# cc-gmail

Gmail CLI for Claude Code: read, send, search, and manage emails from the command line.

**Requirement:** `cc_gmail.exe` must be in PATH (install via `install.bat` in cc-tools repo)

---

## Quick Reference

```bash
# List inbox
cc_gmail list

# Read email
cc_gmail read <message_id>

# Send email
cc_gmail send -t "to@example.com" -s "Subject" -b "Body text"

# Search
cc_gmail search "from:someone@example.com"

# Show profile
cc_gmail profile
```

---

## Commands

### List Emails

```bash
cc_gmail list                    # List inbox (default 10)
cc_gmail list -n 20              # List 20 messages
cc_gmail list -l SENT            # List sent mail
cc_gmail list -l DRAFT           # List drafts
cc_gmail list --unread           # Show unread only
cc_gmail -a work list            # List from 'work' account
```

### Read Email

```bash
cc_gmail read <message_id>       # Read full email
cc_gmail read <message_id> --raw # Show raw data
```

### Send Email

```bash
# Basic send
cc_gmail send -t "to@example.com" -s "Subject" -b "Body text"

# Send with body from file
cc_gmail send -t "to@example.com" -s "Subject" -f body.txt

# Send HTML
cc_gmail send -t "to@example.com" -s "Subject" -f email.html --html

# Send with CC/BCC
cc_gmail send -t "to@example.com" -s "Subject" -b "Body" --cc "cc@example.com" --bcc "bcc@example.com"

# Send with attachments
cc_gmail send -t "to@example.com" -s "Report" -b "See attached" --attach report.pdf --attach data.xlsx

# Send from specific account
cc_gmail -a work send -t "colleague@company.com" -s "Update" -b "Here's the update"
```

### Create Draft

```bash
cc_gmail draft -t "to@example.com" -s "Subject" -b "Draft body"
cc_gmail draft -t "to@example.com" -s "Subject" -f draft.txt
```

### Search

```bash
cc_gmail search "from:boss@company.com"
cc_gmail search "subject:important is:unread"
cc_gmail search "has:attachment after:2024/01/01"
cc_gmail search "in:sent to:client@example.com"
```

### Delete

```bash
cc_gmail delete <message_id>             # Move to trash
cc_gmail delete <message_id> --permanent # Permanently delete
cc_gmail delete <message_id> -y          # Skip confirmation
```

### Labels

```bash
cc_gmail labels                  # List all labels/folders
```

### Profile

```bash
cc_gmail profile                 # Show authenticated user info
```

---

## Multiple Accounts

cc_gmail supports multiple Gmail accounts.

```bash
# List accounts
cc_gmail accounts list

# Add account
cc_gmail accounts add work

# Set default
cc_gmail accounts default work

# Use specific account with any command
cc_gmail -a personal list
cc_gmail --account work send -t "to@example.com" -s "Subject" -b "Body"
```

---

## Gmail Search Syntax

| Query | Description |
|-------|-------------|
| `from:email` | Messages from sender |
| `to:email` | Messages to recipient |
| `subject:word` | Subject contains word |
| `is:unread` | Unread messages |
| `is:starred` | Starred messages |
| `has:attachment` | Has attachments |
| `after:YYYY/MM/DD` | After date |
| `before:YYYY/MM/DD` | Before date |
| `label:name` | Has label |
| `in:inbox` | In inbox |
| `in:sent` | In sent |

Combine queries: `from:boss@company.com subject:report after:2024/01/01`

---

## Authentication

```bash
# Authenticate (opens browser)
cc_gmail auth

# Force re-authentication
cc_gmail auth --force

# Revoke token
cc_gmail auth --revoke
```

---

## Setup (First Time)

1. Create OAuth credentials at Google Cloud Console
2. Enable Gmail API for your project
3. Add account: `cc_gmail accounts add personal`
4. Copy credentials.json to `~/.cc_gmail/accounts/personal/`
5. Run: `cc_gmail auth`

See full setup: https://github.com/CenterConsulting/cc-tools/tree/main/src/cc_gmail

---

## Common Tasks

### Check for new messages
```bash
cc_gmail list --unread -n 5
```

### Find recent emails from someone
```bash
cc_gmail search "from:important@example.com after:2024/01/01" -n 10
```

### Send a quick reply
```bash
cc_gmail send -t "colleague@example.com" -s "Re: Question" -b "Yes, that works for me."
```

### Send document with attachments
```bash
cc_gmail send -t "client@example.com" -s "Documents" -b "Please find attached." --attach doc1.pdf --attach doc2.pdf
```

---

## License

MIT - https://github.com/CenterConsulting/cc-tools
