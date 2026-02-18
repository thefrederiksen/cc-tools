"""Authentication and account management for cc_outlook."""

import json
import logging
from pathlib import Path
from typing import Optional

from O365 import Account
from O365.utils import FileSystemTokenBackend

logger = logging.getLogger(__name__)

# Configuration
CONFIG_DIR = Path.home() / '.cc_outlook'
PROFILES_FILE = CONFIG_DIR / 'profiles.json'
TOKENS_DIR = CONFIG_DIR / 'tokens'

# Delegated permissions - no admin consent required
SCOPES = [
    'https://graph.microsoft.com/Mail.ReadWrite',
    'https://graph.microsoft.com/Mail.Send',
    'https://graph.microsoft.com/Calendars.ReadWrite',
    'https://graph.microsoft.com/User.Read',
    'https://graph.microsoft.com/MailboxSettings.Read',
]


def get_config_dir() -> Path:
    """Get the configuration directory path."""
    return CONFIG_DIR


def get_readme_path() -> Path:
    """Get path to README file."""
    return Path(__file__).parent.parent / 'README.md'


def _ensure_config_dirs() -> None:
    """Create config directories if they don't exist."""
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    TOKENS_DIR.mkdir(parents=True, exist_ok=True)


def _load_profiles() -> dict:
    """Load profiles from file."""
    _ensure_config_dirs()
    if PROFILES_FILE.exists():
        return json.loads(PROFILES_FILE.read_text(encoding='utf-8'))
    return {'profiles': {}, 'default': None}


def _save_profiles(profiles: dict) -> None:
    """Save profiles to file."""
    _ensure_config_dirs()
    PROFILES_FILE.write_text(json.dumps(profiles, indent=2), encoding='utf-8')


def get_token_path(account_name: str) -> Path:
    """Get token file path for an account."""
    safe_name = account_name.replace('@', '_').replace('.', '_')
    return TOKENS_DIR / f'{safe_name}.txt'


def get_account_dir(account_name: str) -> Path:
    """Get account directory path."""
    return CONFIG_DIR


def list_accounts() -> list:
    """
    List all configured accounts.

    Returns:
        List of dicts with account info:
        - name: Account name/email
        - is_default: Whether this is the default account
        - authenticated: Whether token exists and is valid
    """
    profiles = _load_profiles()
    result = []

    for email, profile in profiles.get('profiles', {}).items():
        token_path = Path(profile.get('token_file', ''))

        result.append({
            'name': email,
            'is_default': email == profiles.get('default'),
            'authenticated': token_path.exists(),
            'client_id': profile.get('client_id', '')[:20] + '...' if profile.get('client_id') else '',
        })

    return result


def get_default_account() -> Optional[str]:
    """Get the default account email."""
    profiles = _load_profiles()
    return profiles.get('default')


def set_default_account(account_name: str) -> bool:
    """Set the default account."""
    profiles = _load_profiles()
    if account_name in profiles.get('profiles', {}):
        profiles['default'] = account_name
        _save_profiles(profiles)
        return True
    return False


def resolve_account(account_name: Optional[str] = None) -> str:
    """
    Resolve account name to use.

    Args:
        account_name: Optional explicit account name

    Returns:
        Account name to use

    Raises:
        ValueError: If no account can be resolved
    """
    if account_name:
        profiles = _load_profiles()
        if account_name not in profiles.get('profiles', {}):
            raise ValueError(f"Account '{account_name}' not found. Run 'cc_outlook accounts list' to see available accounts.")
        return account_name

    default = get_default_account()
    if not default:
        raise ValueError("No default account set. Run 'cc_outlook accounts add <email> --client-id <id>' to add an account.")

    return default


def get_profile(account_name: str) -> Optional[dict]:
    """Get profile data for an account."""
    profiles = _load_profiles()
    return profiles.get('profiles', {}).get(account_name)


def save_profile(email: str, client_id: str, tenant_id: str = 'common') -> None:
    """
    Save a new account profile.

    Args:
        email: Email address for the account
        client_id: Azure App Client ID
        tenant_id: Azure Tenant ID (default: 'common')
    """
    _ensure_config_dirs()
    profiles = _load_profiles()

    token_file = str(get_token_path(email))

    profiles['profiles'][email] = {
        'client_id': client_id,
        'tenant_id': tenant_id,
        'token_file': token_file
    }

    # Set as default if it's the first account
    if not profiles.get('default'):
        profiles['default'] = email

    _save_profiles(profiles)


def delete_account(account_name: str) -> bool:
    """
    Delete an account and its token.

    Args:
        account_name: Account email to delete

    Returns:
        True if deleted, False if not found
    """
    profiles = _load_profiles()

    if account_name not in profiles.get('profiles', {}):
        return False

    profile = profiles['profiles'].pop(account_name)

    # Delete token file if it exists
    token_file = Path(profile.get('token_file', ''))
    if token_file.exists():
        token_file.unlink()

    # Update default if needed
    if profiles.get('default') == account_name:
        remaining = list(profiles.get('profiles', {}).keys())
        profiles['default'] = remaining[0] if remaining else None

    _save_profiles(profiles)
    return True


def get_auth_status(account_name: str) -> dict:
    """
    Get detailed authentication status for an account.

    Args:
        account_name: Account email

    Returns:
        Dict with status info
    """
    profile = get_profile(account_name)
    if not profile:
        return {
            'account_dir': str(CONFIG_DIR),
            'token_exists': False,
            'authenticated': False,
            'is_default': False,
        }

    token_path = Path(profile.get('token_file', ''))
    is_authenticated = False

    # Check if token is valid
    if token_path.exists():
        try:
            account = _create_account(profile)
            is_authenticated = account.is_authenticated
        except ValueError as e:
            logger.debug(f"Token validation failed (ValueError): {e}")
            is_authenticated = False
        except KeyError as e:
            logger.debug(f"Token validation failed (KeyError): {e}")
            is_authenticated = False
        except OSError as e:
            logger.debug(f"Token file inaccessible: {e}")
            is_authenticated = False

    return {
        'account_dir': str(CONFIG_DIR),
        'token_exists': token_path.exists(),
        'authenticated': is_authenticated,
        'is_default': account_name == get_default_account(),
        'client_id': profile.get('client_id', '')[:20] + '...',
        'tenant_id': profile.get('tenant_id', 'common'),
    }


def _create_account(profile: dict) -> Account:
    """Create an O365 Account instance from profile data."""
    client_id = profile['client_id']
    tenant_id = profile.get('tenant_id', 'common')
    token_file = profile.get('token_file')

    # Initialize account with public client flow (no client secret)
    credentials = (client_id,)

    # Set up token backend
    token_backend = None
    if token_file:
        token_path = Path(token_file)
        token_backend = FileSystemTokenBackend(
            token_path=token_path.parent,
            token_filename=token_path.name
        )

    return Account(
        credentials,
        tenant_id=tenant_id,
        scopes=SCOPES,
        auth_flow_type='public',
        token_backend=token_backend
    )


def authenticate(account_name: str, force: bool = False) -> Account:
    """
    Authenticate with Outlook/Microsoft Graph.

    Args:
        account_name: Account email
        force: Force re-authentication even if token exists

    Returns:
        Authenticated O365 Account

    Raises:
        ValueError: If account not found
        Exception: If authentication fails
    """
    profile = get_profile(account_name)
    if not profile:
        raise ValueError(f"Account '{account_name}' not found")

    account = _create_account(profile)

    # Check if already authenticated
    if not force and account.is_authenticated:
        return account

    # Delete existing token if forcing
    if force:
        token_path = Path(profile.get('token_file', ''))
        if token_path.exists():
            token_path.unlink()
        # Recreate account with fresh token backend
        account = _create_account(profile)

    # Perform authentication
    if account.authenticate():
        return account
    else:
        raise Exception("Authentication failed. Please try again.")


def revoke_token(account_name: str) -> bool:
    """
    Revoke/delete the token for an account.

    Args:
        account_name: Account email

    Returns:
        True if token was deleted, False if not found
    """
    profile = get_profile(account_name)
    if not profile:
        return False

    token_path = Path(profile.get('token_file', ''))
    if token_path.exists():
        token_path.unlink()
        return True

    return False
