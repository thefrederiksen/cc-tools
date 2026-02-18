# cc_linkedin Skill

LinkedIn CLI tool for interacting with LinkedIn via browser automation.

## When to Use

Use cc_linkedin when the user wants to:
- Check their LinkedIn feed or view posts
- Like or comment on LinkedIn posts
- View LinkedIn profiles
- Send connection requests
- Send messages to connections
- Search for people, posts, or companies on LinkedIn

## Prerequisites

1. **cc_browser daemon must be running** with a LinkedIn profile logged in
2. Start with: `cc-browser daemon --profile linkedin`
3. User must be logged into LinkedIn in that browser session

## Commands

### Status & Authentication
```bash
cc_linkedin status              # Check daemon and login status
cc_linkedin whoami              # Show logged-in user
cc_linkedin me                  # View own profile summary
```

### Feed & Content
```bash
cc_linkedin feed                # View home feed
cc_linkedin feed --limit 5      # Limit results
cc_linkedin post URL            # View specific post
cc_linkedin like URL            # Like a post
cc_linkedin comment URL --text "Great post!"  # Comment on post
cc_linkedin repost URL          # Repost to your feed
cc_linkedin repost URL --thoughts "Great insight!"  # Repost with comment
cc_linkedin save URL            # Save post for later
```

### Profiles & Networking
```bash
cc_linkedin profile USERNAME    # View someone's profile
cc_linkedin connections         # List your connections
cc_linkedin connect USERNAME    # Send connection request
cc_linkedin connect USERNAME --note "Message"  # With note
cc_linkedin company anthropic   # View company page
```

### Invitations
```bash
cc_linkedin invitations         # View pending connection requests
cc_linkedin accept "John"       # Accept invitation from John
cc_linkedin ignore "John"       # Ignore invitation from John
```

### Notifications
```bash
cc_linkedin notifications       # View all notifications
cc_linkedin notifications --unread  # Show only unread
```

### Messaging
```bash
cc_linkedin messages            # View recent messages
cc_linkedin messages --unread   # Show only unread messages
cc_linkedin message USERNAME --text "Hello!"  # Send message
```

### Search & Jobs
```bash
cc_linkedin search "query"                    # Search all
cc_linkedin search "query" --type people      # Search people
cc_linkedin search "query" --type posts       # Search posts
cc_linkedin search "query" --type companies   # Search companies
cc_linkedin jobs "AI engineer"                # Search for jobs
cc_linkedin jobs "Python" --location "Remote" # Jobs with location
```

### Navigation & Debug
```bash
cc_linkedin goto URL            # Navigate to URL
cc_linkedin snapshot            # Get page snapshot
cc_linkedin screenshot          # Take screenshot
```

## Global Options

- `--port INT`: cc_browser daemon port (default 9280)
- `--format TEXT`: Output format (text/json/markdown)
- `--delay FLOAT`: Delay between actions (default 1.0)
- `-v, --verbose`: Verbose output for debugging

## Usage Patterns

### Check Activity
```bash
# Ensure daemon is running
cc_linkedin status

# Check notifications
cc_linkedin notifications --unread

# View feed
cc_linkedin feed --limit 10
```

### Engage with Content
```bash
# View a post
cc_linkedin post "https://www.linkedin.com/feed/update/urn:li:activity:1234567890"

# Like it
cc_linkedin like "https://www.linkedin.com/feed/update/urn:li:activity:1234567890"

# Comment
cc_linkedin comment "https://www.linkedin.com/feed/update/urn:li:activity:1234567890" --text "Great insights!"

# Repost with your thoughts
cc_linkedin repost "https://www.linkedin.com/feed/update/urn:li:activity:1234567890" --thoughts "Must read!"

# Save for later
cc_linkedin save "https://www.linkedin.com/feed/update/urn:li:activity:1234567890"
```

### Manage Invitations
```bash
# Check pending invitations
cc_linkedin invitations

# Accept specific person
cc_linkedin accept "John Smith"

# Ignore spam
cc_linkedin ignore "Recruiter"
```

### Networking Workflow
```bash
# Search for relevant people
cc_linkedin search "software engineer at Microsoft" --type people

# View their profile
cc_linkedin profile johndoe

# Research their company
cc_linkedin company microsoft

# Send connection request
cc_linkedin connect johndoe --note "Hi! I noticed we share similar interests in cloud architecture."
```

### Job Search
```bash
# Search for jobs
cc_linkedin jobs "AI engineer" --location "San Francisco"

# Search remote jobs
cc_linkedin jobs "Python developer" --location "Remote"
```

### Messaging
```bash
# Check unread messages
cc_linkedin messages --unread

# Send a message
cc_linkedin message janedoe --text "Thanks for connecting! Would love to chat about your recent project."
```

## Output Formats

```bash
# Default text output
cc_linkedin feed

# JSON output (for parsing)
cc_linkedin feed --format json

# Markdown output
cc_linkedin profile johndoe --format markdown
```

## Troubleshooting

### "Cannot connect to cc_browser daemon"
- Start the daemon: `cc-browser daemon --profile linkedin`

### "Not logged in"
- Open LinkedIn in the browser and log in
- The browser session persists with the profile

### "Could not find button"
- LinkedIn's UI changes frequently
- Use `cc_linkedin snapshot` to see available elements
- Report issues if selectors need updating

## Notes

- All interactions happen through browser automation (like a real user)
- No API keys required - uses existing browser session
- Rate limiting: Use `--delay` option to avoid triggering LinkedIn's detection
- LinkedIn may require CAPTCHA verification occasionally
