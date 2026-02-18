# cc_outlook

Outlook CLI for Claude Code: read, send, search emails and manage calendar from the command line.

## Installation

1. Build the executable:
   ```powershell
   cd src\cc_outlook
   .\build.ps1
   ```

2. The executable will be at `dist\cc_outlook.exe`

3. Run the central build script to copy to `C:\cc_tools\`:
   ```batch
   scripts\build.bat
   ```

## Quick Start

### 1. Set Up Azure App (One-Time)

1. Go to https://portal.azure.com
2. Search for "App registrations" -> "+ New registration"
3. Settings:
   - Name: `cc_outlook_cli`
   - Account types: "Accounts in any organizational directory and personal Microsoft accounts"
   - Redirect URI: Mobile and desktop -> `http://localhost`
4. Copy the Application (client) ID
5. Go to API permissions -> Add: Mail.ReadWrite, Mail.Send, Calendars.ReadWrite, User.Read, MailboxSettings.Read
6. Go to Authentication -> Add URI: `https://login.microsoftonline.com/common/oauth2/nativeclient`
7. Enable "Allow public client flows"

See [docs/AUTHENTICATION.md](docs/AUTHENTICATION.md) for detailed setup instructions.

### 2. Add Your Account

```bash
cc_outlook accounts add your@email.com --client-id YOUR_CLIENT_ID
```

### 3. Authenticate

```bash
cc_outlook auth
```

**IMPORTANT:** During authentication, you'll see "This is not the right page" - this is normal! Copy the URL and paste it back in the terminal.

## Usage

### Email Commands

```bash
# List emails
cc_outlook list                    # List inbox (default 10)
cc_outlook list -n 20              # List 20 messages
cc_outlook list -f sent            # List sent mail
cc_outlook list --unread           # Show unread only

# Read email
cc_outlook read <message_id>

# Send email
cc_outlook send -t "to@example.com" -s "Subject" -b "Body text"
cc_outlook send -t "to@example.com" -s "Subject" -b "Body" --cc "cc@example.com"
cc_outlook send -t "to@example.com" -s "Subject" -b "Body" --bcc "bcc@example.com"
cc_outlook send -t "to@example.com" -s "Subject" -b "<h1>HTML</h1>" --html
cc_outlook send -t "to@example.com" -s "Subject" -b "Urgent!" --importance high

# Reply/Forward
cc_outlook reply <message_id> -b "Thanks for the info"
cc_outlook reply <message_id> -b "Thanks all" --all  # Reply all
cc_outlook forward <message_id> -t "other@example.com" -b "FYI"

# Search
cc_outlook search "project update"

# Delete
cc_outlook delete <message_id>

# Flag and categorize
cc_outlook flag <message_id>                    # Flag for follow-up
cc_outlook flag <message_id> -s complete        # Mark complete
cc_outlook flag <message_id> -d 2024-12-31      # Flag with due date
cc_outlook categorize <message_id> "Work,Urgent"

# Attachments
cc_outlook attachments <message_id>                           # List attachments
cc_outlook download-attachment <message_id> <attachment_id>   # Download

# Folders
cc_outlook folders
```

### Calendar Commands

```bash
# View events
cc_outlook calendar events         # Next 7 days
cc_outlook calendar events -d 14   # Next 14 days

# View event details
cc_outlook calendar get <event_id>

# Create event
cc_outlook calendar create -s "Meeting" -d 2024-12-25 -t 14:00
cc_outlook calendar create -s "Meeting" -d 2024-12-25 -t 14:00 --duration 90
cc_outlook calendar create -s "Meeting" -d 2024-12-25 -t 14:00 -l "Room 101"
cc_outlook calendar create -s "Meeting" -d 2024-12-25 -t 14:00 --attendees "a@ex.com,b@ex.com"
cc_outlook calendar create -s "Holiday" -d 2024-12-25 -t 00:00 --all-day

# Update event
cc_outlook calendar update <event_id> -s "New Subject"
cc_outlook calendar update <event_id> -l "New Location"
cc_outlook calendar update <event_id> -d 2024-12-26 -t 15:00

# Respond to invitations
cc_outlook calendar respond <event_id> accept
cc_outlook calendar respond <event_id> decline -m "Sorry, I'm busy"
cc_outlook calendar respond <event_id> tentative

# Delete event
cc_outlook calendar delete <event_id>
```

### Account Management

```bash
# List accounts
cc_outlook accounts list

# Add account
cc_outlook accounts add work@company.com --client-id YOUR_CLIENT_ID

# Set default
cc_outlook accounts default work@company.com

# Use specific account
cc_outlook -a work list
```

## Configuration

Configuration is stored in `~/.cc_outlook/`:

| File | Purpose |
|------|---------|
| `profiles.json` | Account configurations |
| `tokens/` | OAuth tokens |

## Troubleshooting

### "Reply URL does not match"

Add both redirect URIs in Azure:
- `https://login.microsoftonline.com/common/oauth2/nativeclient`
- `http://localhost`

### "This is not the right page"

This is normal! The URL bar should show `nativeclient?code=...` - copy that full URL and paste it in the terminal.

### Redirected to "wrongplace" (no code in URL)

If the URL shows `wrongplace` instead of `nativeclient?code=...`:
- OAuth state mismatch - browser session doesn't match what cc_outlook expects
- Run `cc_outlook auth --force` in a fresh terminal
- Complete login manually in browser (don't use browser automation)
- Copy the redirect URL back to the SAME terminal

### Token expired

```bash
cc_outlook auth --force
```

See [docs/AUTHENTICATION.md](docs/AUTHENTICATION.md) for more troubleshooting.

## Development

### Project Structure

```
src/cc_outlook/
  src/
    __init__.py      # Version info
    __main__.py      # Module entry point
    cli.py           # Typer CLI commands
    auth.py          # Authentication logic
    outlook_api.py   # O365 API wrapper
    utils.py         # Helper functions
  docs/
    AUTHENTICATION.md
  tests/
  main.py            # PyInstaller entry point
  build.ps1          # Build script
  cc_outlook.spec    # PyInstaller spec
  pyproject.toml     # Package config
  requirements.txt   # Dependencies
```

### Building

```powershell
.\build.ps1
```

### Testing

```bash
pytest tests/
```

## License

MIT
