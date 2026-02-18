# cc_outlook Authentication Guide

## Overview

cc_outlook uses Microsoft Graph API via the O365 library with OAuth 2.0 public client flow.
This guide walks you through the complete setup process.

## Quick Reference

Already set up? Here are the common commands:

```bash
cc_outlook list                     # List inbox emails
cc_outlook list --unread            # List unread emails only
cc_outlook calendar events          # View calendar for next 7 days
cc_outlook folders                  # List mail folders
cc_outlook send -t email@example.com -s "Hi" -b "Hello"
cc_outlook auth                     # Re-authenticate if needed
```

---

## Part 1: Azure App Registration (One-Time Setup)

You only need to do this ONCE. The same app registration works for multiple email accounts.

### Step 1: Open Azure Portal

1. Go to **https://portal.azure.com**
2. Sign in with your Microsoft account

### Step 2: Navigate to App Registrations

1. In the **search bar at the top**, type: `App registrations`
2. Click on **App registrations** in the results
3. Click **+ New registration**

### Step 3: Fill in the Registration Form

| Field | Value |
|-------|-------|
| **Name** | `cc_outlook_cli` |
| **Supported account types** | Select: **Accounts in any organizational directory and personal Microsoft accounts** |

**IMPORTANT - Redirect URI:**

| Field | Value |
|-------|-------|
| **Platform** | Select: **Mobile and desktop applications** |
| **URI** | Enter: `http://localhost` |

Click **Register**

### Step 4: Copy the Application (Client) ID

After registration, you'll see the app overview page.

1. Find **Application (client) ID** in the Essentials section
2. **Copy this value** - you'll need it later
3. It looks like: `YOUR_CLIENT_ID`

### Step 5: Add API Permissions

1. In the left menu, click **API permissions**
2. Click **+ Add a permission**
3. Click **Microsoft Graph**
4. Click **Delegated permissions**
5. Search and **check** each of these (one at a time):
   - `Mail.ReadWrite`
   - `Mail.Send`
   - `Calendars.ReadWrite`
   - `User.Read`
   - `MailboxSettings.Read`
6. Click **Add permissions**

Your permissions list should show:

```
Microsoft Graph (5)
  Calendars.ReadWrite      Delegated    No
  Mail.ReadWrite           Delegated    No
  Mail.Send                Delegated    No
  MailboxSettings.Read     Delegated    No
  User.Read                Delegated    No
```

### Step 6: Add Second Redirect URI (CRITICAL)

This step is **essential** - without it you'll get redirect errors.

1. In the left menu, click **Authentication**
2. Under **Mobile and desktop applications**, click **Add URI** or the existing row
3. **Add** this URI (in addition to http://localhost):
   ```
   https://login.microsoftonline.com/common/oauth2/nativeclient
   ```
4. Click **Save**

You should now have **TWO** redirect URIs:
- `https://login.microsoftonline.com/common/oauth2/nativeclient`
- `http://localhost`

### Step 7: Enable Public Client Flow

1. Still on the **Authentication** page
2. Scroll down to **Advanced settings**
3. Find **Allow public client flows**
4. Set it to **Yes** (toggle should be enabled)
5. Click **Save**

---

## Part 2: Connect Your Account

### Add an Account

```bash
cc_outlook accounts add YOUR_EMAIL --client-id YOUR_CLIENT_ID
```

Example:
```bash
cc_outlook accounts add user@example.com --client-id YOUR_CLIENT_ID
```

### Authenticate

```bash
cc_outlook auth
```

### The Authentication Flow

**IMPORTANT - Read this carefully!**

1. A URL is displayed in the terminal and a browser window opens
2. **Sign in** with your Microsoft account
3. **Accept the permissions** when prompted
4. **You'll see a page that says "This is not the right page"** - **THIS IS NORMAL**
5. **Copy the ENTIRE URL** from your browser's address bar (Ctrl+L, Ctrl+C)
   - The URL looks like: `https://login.microsoftonline.com/common/oauth2/nativeclient?code=0.AXYA...`
6. **Go back to the terminal** and paste the URL
7. **Press Enter**

You should see:
```
Authentication Flow Completed. Oauth Access Token Stored. You can now use the API.
[green]Authenticated as:[/green] your.email@domain.com
```

---

## Part 3: Using cc_outlook

### Email Commands

```bash
# List emails
cc_outlook list                    # List inbox (default 10)
cc_outlook list -n 20              # List 20 messages
cc_outlook list -f sent            # List sent mail
cc_outlook list --unread           # Show unread only

# Read email
cc_outlook read <message_id>       # Read full email

# Send email
cc_outlook send -t "to@example.com" -s "Subject" -b "Body text"
cc_outlook send -t "to@example.com" -s "Subject" -f body.txt
cc_outlook send -t "to@example.com" -s "Report" -b "See attached" --attach report.pdf

# Create draft
cc_outlook draft -t "to@example.com" -s "Subject" -b "Draft body"

# Search
cc_outlook search "quarterly report"
cc_outlook search "from:sender" -n 20

# Delete
cc_outlook delete <message_id>             # Delete message
cc_outlook delete <message_id> -y          # Skip confirmation
```

### Calendar Commands

```bash
# List calendars
cc_outlook calendar list

# View events
cc_outlook calendar events         # Next 7 days
cc_outlook calendar events -d 14   # Next 14 days
cc_outlook calendar events -c "Work Calendar"

# Create event
cc_outlook calendar create -s "Meeting" -d 2024-12-25 -t 14:00
cc_outlook calendar create -s "Meeting" -d 2024-12-25 -t 14:00 --duration 90
cc_outlook calendar create -s "Meeting" -d 2024-12-25 -t 14:00 -l "Room A"
cc_outlook calendar create -s "Meeting" -d 2024-12-25 -t 14:00 --attendees "a@x.com,b@x.com"
```

### Multiple Accounts

```bash
# List accounts
cc_outlook accounts list

# Add another account (same client ID works)
cc_outlook accounts add another@email.com --client-id YOUR_CLIENT_ID

# Set default
cc_outlook accounts default another@email.com

# Use specific account
cc_outlook -a personal list
cc_outlook --account work send -t "to@example.com" -s "Subject" -b "Body"
```

---

## Part 4: Troubleshooting

### Error: AADSTS50011 - Reply URL does not match

**Cause:** Missing redirect URI in Azure.

**Solution:**
1. Go to Azure Portal -> App registrations -> your app -> Authentication
2. Make sure BOTH redirect URIs are configured:
   - `https://login.microsoftonline.com/common/oauth2/nativeclient`
   - `http://localhost`

### Error: AADSTS65001 - User has not consented

**Cause:** Permissions not accepted.

**Solution:**
1. Re-run `cc_outlook auth --force`
2. Make sure to click "Accept" on the consent screen

### "This is not the right page" in browser

**This is NORMAL.** You need to:
1. Copy the entire URL from the browser address bar
2. Paste it back into the terminal
3. Press Enter

The URL should look like:
```
https://login.microsoftonline.com/common/oauth2/nativeclient?code=0.AXYA...&state=...
```

The URL contains the authorization code that the tool needs.

### Redirected to "wrongplace" (no code in URL)

If you see `https://login.microsoftonline.com/common/wrongplace` in the browser URL bar:

**Cause:** OAuth state mismatch. The browser session completed authentication but the state parameter doesn't match what cc_outlook expects. This commonly happens when:
- Using browser automation to complete the OAuth flow
- The browser has cached SSO sessions that auto-complete login
- Running multiple auth attempts without completing them

**Solution:**
1. Close the browser tab
2. Run `cc_outlook auth --force` in a fresh terminal
3. When the browser opens, complete the login manually
4. The URL bar should show `nativeclient?code=...` (NOT `wrongplace`)
5. Copy that URL and paste it back into the SAME terminal

If still failing:
- Clear cookies for `login.microsoftonline.com` in your browser
- Or use an incognito/private browser window
- Or try a different browser

**IMPORTANT:** Do NOT use browser automation (Playwright, cc-browser, etc.) to complete OAuth flows - it causes state mismatch issues.

### Token expired / Authentication required again

Tokens expire after ~90 days of inactivity.

**Solution:**
```bash
# Revoke and re-authenticate
cc_outlook auth --revoke
cc_outlook auth
```

Or manually delete the token file:
```bash
# Windows
del "%USERPROFILE%\.cc_outlook\tokens\your_email_domain_com.txt"

# Then re-authenticate
cc_outlook auth
```

### Error: Account not found

**Solution:**
```bash
# List accounts to see what's configured
cc_outlook accounts list

# Add the account if missing
cc_outlook accounts add your@email.com --client-id YOUR_CLIENT_ID
```

---

## Part 5: File Locations

| Item | Location |
|------|----------|
| Profiles | `%USERPROFILE%\.cc_outlook\profiles.json` |
| Tokens | `%USERPROFILE%\.cc_outlook\tokens\` |

---

## Part 6: Azure App Settings Summary

For reference, here are all the Azure app settings needed:

### App Registration

| Setting | Value |
|---------|-------|
| Name | `cc_outlook_cli` |
| Supported account types | Accounts in any organizational directory and personal Microsoft accounts |

### Redirect URIs (Mobile and desktop applications)

Both of these MUST be configured:
```
https://login.microsoftonline.com/common/oauth2/nativeclient
http://localhost
```

### API Permissions (Microsoft Graph - Delegated)

| Permission | Description |
|------------|-------------|
| Mail.ReadWrite | Read and write mail |
| Mail.Send | Send mail |
| Calendars.ReadWrite | Read and write calendars |
| User.Read | Read user profile |
| MailboxSettings.Read | Read mailbox settings |

### Authentication Settings

| Setting | Value |
|---------|-------|
| Allow public client flows | **Yes** (Enabled) |

---

## Appendix: Known Working Client IDs

| Account Type | Client ID |
|--------------|-----------|
| example (multi-tenant) | `YOUR_CLIENT_ID` |

The same Client ID can be used for multiple accounts if the app is registered as multi-tenant.
