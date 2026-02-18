# cc_reddit

Reddit CLI via browser automation. Read posts, comment, vote, and manage subreddits.

**Requirements:**
- `cc_reddit` must be available (Python)
- cc_browser daemon must be running
- Logged into Reddit in the browser

---

## Quick Reference

```bash
# Check status
cc_reddit status

# Check login
cc_reddit whoami

# View subreddit feed
cc_reddit feed python

# View a post
cc_reddit post URL

# Navigate to subreddit
cc_reddit goto r/programming
```

---

## Setup

```bash
# 1. Start cc_browser daemon
cc-browser daemon

# 2. Start browser and log into Reddit manually
cc-browser start
cc-browser navigate --url "https://reddit.com/login"
# Log in manually in the browser

# 3. Now cc_reddit commands will work
cc_reddit whoami
```

---

## Commands

### Status & Login

```bash
# Check daemon and browser status
cc_reddit status

# Check logged-in username
cc_reddit whoami
```

### Navigation

```bash
# Go to subreddit
cc_reddit goto r/python
cc_reddit goto programming  # r/ prefix optional

# Go to user profile
cc_reddit goto u/username

# Go to any Reddit URL
cc_reddit goto "https://reddit.com/r/python/hot"
```

### Reading

```bash
# View subreddit feed
cc_reddit feed python
cc_reddit feed home          # Front page
cc_reddit feed python --sort new
cc_reddit feed python --sort top
cc_reddit feed python --limit 20

# View a specific post
cc_reddit post URL
cc_reddit post "https://reddit.com/r/python/comments/abc123"
```

### Commenting

```bash
# Comment on a post
cc_reddit comment URL --text "Great post!"
cc_reddit comment URL -t "I agree with this point"
```

### Voting

```bash
# Upvote
cc_reddit upvote URL

# Downvote
cc_reddit downvote URL
```

### Subreddit Management

```bash
# Join a subreddit
cc_reddit join python

# Leave a subreddit
cc_reddit leave python
```

### Utilities

```bash
# Get page snapshot (for debugging)
cc_reddit snapshot

# Take screenshot
cc_reddit screenshot --output reddit.png
```

---

## Options

| Option | Description |
|--------|-------------|
| `--port` | cc_browser daemon port (default: 9280) |
| `--format` | Output format: text, json, markdown |
| `--delay` | Delay between actions (seconds) |
| `-v, --verbose` | Verbose output |

---

## Feed Sorting

| Sort | Description |
|------|-------------|
| `hot` | Hot posts (default) |
| `new` | Newest posts |
| `top` | Top posts |
| `rising` | Rising posts |

---

## Examples

### Browse Reddit

```bash
# Check what subreddits have interesting content
cc_reddit feed programming --sort hot --limit 10
cc_reddit feed python --sort top
```

### Read and Comment

```bash
# 1. Find an interesting post
cc_reddit feed learnpython --limit 5

# 2. Read a post
cc_reddit post "https://reddit.com/r/learnpython/comments/abc123"

# 3. Comment
cc_reddit comment "https://reddit.com/r/learnpython/comments/abc123" \
  --text "Here's a tip: use list comprehensions for this!"
```

### Manage Subscriptions

```bash
# Join interesting subreddits
cc_reddit join machinelearning
cc_reddit join datascience
cc_reddit join python

# Leave one you don't like
cc_reddit leave memes
```

### Upvote Good Content

```bash
cc_reddit upvote "https://reddit.com/r/python/comments/helpful_post"
```

---

## Tips

1. **Login first** - Use cc_browser to log into Reddit before using cc_reddit
2. **Rate limiting** - Reddit may rate-limit rapid actions; use `--delay` if needed
3. **Verbose mode** - Use `-v` to see what elements are being detected
4. **Snapshot** - Use `cc_reddit snapshot` to debug element detection issues

---

## Requires cc_browser

cc_reddit uses cc_browser for browser automation. Ensure:
1. cc_browser daemon is running (`cc-browser daemon`)
2. Browser is started (`cc-browser start`)
3. You're logged into Reddit in the browser

---

## LLM Use Cases

1. **Reddit browsing** - "Check the top posts in r/programming"
2. **Research** - "Find recent posts about Python asyncio"
3. **Engagement** - "Upvote this helpful answer"
4. **Community management** - "Join these subreddits for learning"
5. **Posting** - "Comment on this post with my response"
