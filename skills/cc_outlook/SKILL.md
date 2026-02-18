# cc_outlook

Outlook CLI for Claude Code: read, send, search emails and manage calendar from the command line.

**Requirement:** `cc_outlook.exe` must be in PATH (install via `install.bat` in cc_tools repo)

---

## CRITICAL: Authentication Setup

Before using cc_outlook, you MUST set up Azure authentication:

### Azure App Registration (One-Time)

1. Go to https://portal.azure.com
2. Search "App registrations" -> "+ New registration"
3. Settings:
   - Name: `cc_outlook_cli`
   - Account types: **Accounts in any organizational directory and personal Microsoft accounts**
   - Redirect URI: Mobile and desktop -> `http://localhost`
4. Copy the **Application (client) ID**
5. API permissions -> Add (Delegated): `Mail.ReadWrite`, `Mail.Send`, `Calendars.ReadWrite`, `User.Read`, `MailboxSettings.Read`
6. **CRITICAL**: Authentication -> Add URI: `https://login.microsoftonline.com/common/oauth2/nativeclient`
7. Enable: **Allow public client flows** = Yes

### Add Account

```bash
cc_outlook accounts add your@email.com --client-id YOUR_CLIENT_ID
cc_outlook auth
```

### Authentication Flow - IMPORTANT

During `cc_outlook auth`:
1. Browser opens -> Sign in -> Accept permissions
2. **You'll see "This is not the right page"** - THIS IS NORMAL
3. **Copy the ENTIRE URL** from the browser address bar
4. **Paste it into the terminal** and press Enter

---

## Quick Reference

```bash
# List inbox
cc_outlook list

# Read email
cc_outlook read <message_id>

# Send email
cc_outlook send -t "to@example.com" -s "Subject" -b "Body text"

# Search
cc_outlook search "project update"

# Show profile
cc_outlook profile

# Calendar events
cc_outlook calendar events
```

---

## Email Commands

### List Emails

```bash
cc_outlook list                    # List inbox (default 10)
cc_outlook list -n 20              # List 20 messages
cc_outlook list -f sent            # List sent mail
cc_outlook list -f drafts          # List drafts
cc_outlook list --unread           # Show unread only
cc_outlook -a work list            # List from 'work' account
```

### Read Email

```bash
cc_outlook read <message_id>       # Read full email
cc_outlook read <message_id> --raw # Show raw data
```

### Send Email

```bash
# Basic send
cc_outlook send -t "to@example.com" -s "Subject" -b "Body text"

# Send with body from file
cc_outlook send -t "to@example.com" -s "Subject" -f body.txt

# Send HTML
cc_outlook send -t "to@example.com" -s "Subject" -f email.html --html

# Send with CC/BCC
cc_outlook send -t "to@example.com" -s "Subject" -b "Body" --cc "cc@example.com" --bcc "bcc@example.com"

# Send with attachments
cc_outlook send -t "to@example.com" -s "Report" -b "See attached" --attach report.pdf --attach data.xlsx

# Send with importance
cc_outlook send -t "to@example.com" -s "Urgent" -b "Important" --importance high

# Send from specific account
cc_outlook -a work send -t "colleague@company.com" -s "Update" -b "Here's the update"
```

### Create Draft

```bash
cc_outlook draft -t "to@example.com" -s "Subject" -b "Draft body"
cc_outlook draft -t "to@example.com" -s "Subject" -f draft.txt
```

### Search

```bash
cc_outlook search "quarterly report"
cc_outlook search "from sender" -n 20
cc_outlook search "invoice" -f sent
```

### Delete

```bash
cc_outlook delete <message_id>             # Delete message
cc_outlook delete <message_id> --permanent # Permanently delete
cc_outlook delete <message_id> -y          # Skip confirmation
```

### Folders

```bash
cc_outlook folders                 # List all folders with counts
```

### Profile

```bash
cc_outlook profile                 # Show authenticated user info
```

---

## Calendar Commands

### List Calendars

```bash
cc_outlook calendar list
```

### View Events

```bash
cc_outlook calendar events         # Next 7 days
cc_outlook calendar events -d 14   # Next 14 days
cc_outlook calendar events -c "Work Calendar"
```

### Create Event

```bash
# Basic event (60 min default)
cc_outlook calendar create -s "Meeting" -d 2024-12-25 -t 14:00

# With duration
cc_outlook calendar create -s "Meeting" -d 2024-12-25 -t 14:00 --duration 90

# With location
cc_outlook calendar create -s "Meeting" -d 2024-12-25 -t 14:00 -l "Room A"

# With attendees
cc_outlook calendar create -s "Meeting" -d 2024-12-25 -t 14:00 --attendees "a@x.com,b@x.com"

# All-day event
cc_outlook calendar create -s "Holiday" -d 2024-12-25 -t 00:00 --all-day
```

---

## Multiple Accounts

cc_outlook supports multiple Outlook accounts.

```bash
# List accounts
cc_outlook accounts list

# Add account
cc_outlook accounts add work --client-id YOUR_CLIENT_ID

# Set default
cc_outlook accounts default work

# Use specific account with any command
cc_outlook -a personal list
cc_outlook --account work send -t "to@example.com" -s "Subject" -b "Body"
```

---

## Authentication

```bash
# Authenticate (opens browser)
cc_outlook auth

# Force re-authentication
cc_outlook auth --force

# Revoke token
cc_outlook auth --revoke
```

---

## Troubleshooting

### "Reply URL does not match" Error

Add BOTH redirect URIs in Azure Authentication:
- `https://login.microsoftonline.com/common/oauth2/nativeclient`
- `http://localhost`

### "This is not the right page"

THIS IS NORMAL! Copy the URL and paste it in the terminal.

### Token Expired

```bash
cc_outlook auth --force
```

### Account Not Found

```bash
cc_outlook accounts add your@email.com --client-id YOUR_CLIENT_ID
cc_outlook auth
```

---

## Common Tasks

### Check for new messages
```bash
cc_outlook list --unread -n 5
```

### Send a quick reply
```bash
cc_outlook send -t "colleague@example.com" -s "Re: Question" -b "Yes, that works for me."
```

### Send document with attachments
```bash
cc_outlook send -t "client@example.com" -s "Documents" -b "Please find attached." --attach doc1.pdf --attach doc2.pdf
```

### View upcoming meetings
```bash
cc_outlook calendar events -d 3
```

### Schedule a meeting
```bash
cc_outlook calendar create -s "Project Review" -d 2024-12-20 -t 10:00 --duration 60 --attendees "team@company.com"
```

---

## Configuration

| Location | Purpose |
|----------|---------|
| `~/.cc_outlook/profiles.json` | Account configurations |
| `~/.cc_outlook/tokens/` | OAuth tokens |

---

## License

MIT - https://github.com/CenterConsulting/cc_tools
