# cc_reddit

A command-line tool for Reddit interactions via browser automation.

## Overview

cc_reddit enables programmatic Reddit interactions through browser automation, acting exactly like a human user. No API keys required.

**Key Features:**
- Browse subreddits and posts
- Create posts and comments
- Vote, save, and engage with content
- Manage subscriptions
- Send and receive messages
- Moderation tools (for moderators)

## Requirements

- cc_browser daemon running (port 9280)
- Chrome/Edge browser
- Logged into Reddit in the browser

## Quick Start

```bash
# Start cc_browser daemon
cc-browser start --profile reddit

# Check Reddit login status
cc_reddit status

# Show current user
cc_reddit whoami

# View subreddit feed
cc_reddit feed programming --limit 10

# View a post
cc_reddit post "https://reddit.com/r/programming/comments/abc123/..."

# Create a post
cc_reddit post create learnpython --title "Question about loops" --body "How do I..."

# Comment on a post
cc_reddit comment abc123 --text "Great explanation!"

# Upvote
cc_reddit upvote abc123
```

## Commands

### Status & Authentication
| Command | Description |
|---------|-------------|
| `status` | Check if logged into Reddit |
| `whoami` | Show current username |

### Reading
| Command | Description |
|---------|-------------|
| `feed [SUBREDDIT]` | View subreddit feed |
| `post [URL]` | View post content |
| `comments [URL]` | View post comments |
| `search [QUERY]` | Search Reddit |
| `user [USERNAME]` | View user profile |
| `inbox` | View messages |
| `saved` | View saved items |

### Writing
| Command | Description |
|---------|-------------|
| `post create` | Create new post |
| `comment` | Comment on post |
| `reply` | Reply to comment |
| `edit` | Edit post/comment |
| `delete` | Delete post/comment |

### Engagement
| Command | Description |
|---------|-------------|
| `upvote` | Upvote post/comment |
| `downvote` | Downvote post/comment |
| `save` | Save post/comment |
| `join` | Join subreddit |
| `leave` | Leave subreddit |

### Messaging
| Command | Description |
|---------|-------------|
| `message` | Send direct message |

### Moderation
| Command | Description |
|---------|-------------|
| `mod approve` | Approve item |
| `mod remove` | Remove item |
| `mod ban` | Ban user |
| `mod queue` | View modqueue |

## Options

```
--profile TEXT    Browser profile (default: reddit)
--format TEXT     Output: text, json, markdown
--delay FLOAT     Delay between actions (seconds)
--verbose         Detailed output
```

## Browser Setup

1. Start cc_browser with a profile for Reddit:
   ```bash
   cc-browser start --profile reddit
   ```

2. Log into Reddit in the browser window that opens

3. Your session persists - cc_reddit uses the same browser session

## How It Works

```
cc_reddit (Python CLI)
    |
    | HTTP requests to localhost:9280
    v
cc_browser daemon (Node.js)
    |
    | Chrome DevTools Protocol
    v
Chrome browser (logged into Reddit)
```

## Part of cc_tools

This tool is part of the [cc_tools](https://github.com/sfrederico/cc_tools) suite.
