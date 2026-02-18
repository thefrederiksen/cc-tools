# cc_tools

A suite of command-line tools for document conversion, media processing, and AI-powered workflows.

**GitHub:** https://github.com/CenterConsulting/cc_tools

---

## Available Tools

| Tool | Description | Status |
|------|-------------|--------|
| cc_crawl4ai | AI-ready web crawler | Available |
| cc_gmail | Gmail CLI: read, send, search emails | Available |
| cc_image | Image generation/analysis/OCR | Coming Soon |
| cc_markdown | Markdown to PDF/Word/HTML | Available |
| cc_outlook | Outlook CLI: read, send, search emails, calendar | Available |
| cc_transcribe | Video/audio transcription | Available |
| cc_video | Video utilities | Coming Soon |
| cc_voice | Text-to-speech | Coming Soon |
| cc_whisper | Audio transcription | Coming Soon |
| cc_youtube_info | YouTube transcript/metadata extraction | Available |

---

## cc_markdown

Convert Markdown to beautifully styled PDF, Word, and HTML documents.

### Usage

```bash
# Convert to PDF with a theme
cc_markdown report.md -o report.pdf --theme boardroom

# Convert to Word
cc_markdown report.md -o report.docx --theme paper

# Convert to HTML
cc_markdown report.md -o report.html

# Use custom CSS
cc_markdown report.md -o report.pdf --css custom.css

# List available themes
cc_markdown --themes
```

### Available Themes

- **boardroom** - Corporate, executive style
- **terminal** - Technical, monospace
- **paper** - Minimal, clean
- **spark** - Creative, colorful
- **thesis** - Academic, scholarly
- **obsidian** - Dark theme
- **blueprint** - Technical documentation

### Options

| Option | Description |
|--------|-------------|
| `-o, --output` | Output file path (format detected from extension) |
| `--theme` | Built-in theme name |
| `--css` | Path to custom CSS file |
| `--page-size` | Page size: a4, letter (default: a4) |
| `--margin` | Page margin (default: 1in) |
| `--themes` | List available themes |
| `--version` | Show version |
| `--help` | Show help |

### Examples

```bash
# Basic PDF
cc_markdown README.md -o README.pdf

# Corporate report
cc_markdown quarterly-report.md -o report.pdf --theme boardroom

# Technical documentation
cc_markdown api-docs.md -o api-docs.pdf --theme blueprint

# Academic paper
cc_markdown thesis.md -o thesis.pdf --theme thesis --page-size letter
```

---

## cc_transcribe

Video and audio transcription with timestamps and automatic screenshot extraction.

**Requirements:**
- FFmpeg must be installed and in PATH
- OpenAI API key: set `OPENAI_API_KEY` environment variable

### Usage

```bash
# Basic transcription
cc_transcribe video.mp4

# Specify output directory
cc_transcribe video.mp4 -o ./output/

# Without screenshots
cc_transcribe video.mp4 --no-screenshots

# Adjust screenshot sensitivity (lower = more screenshots)
cc_transcribe video.mp4 --threshold 0.85 --interval 2.0

# Force language
cc_transcribe video.mp4 --language en

# Show video info only
cc_transcribe video.mp4 --info
```

### Output Structure

```
output_directory/
    transcript.txt      # Timestamped transcript
    transcript.json     # Detailed segments with timing
    screenshots/        # Extracted frames
        screenshot_00-00-00.png
        screenshot_00-01-23.png
        ...
```

### Options

| Option | Description |
|--------|-------------|
| `-o, --output` | Output directory |
| `--no-screenshots` | Skip screenshot extraction |
| `--threshold` | SSIM threshold 0.0-1.0 (default: 0.92, lower = more screenshots) |
| `--interval` | Minimum seconds between screenshots (default: 1.0) |
| `--language` | Force language code (e.g., en, es, fr) |
| `--info` | Show video info and exit |
| `--help` | Show help |

### Examples

```bash
# Transcribe a meeting recording
cc_transcribe meeting.mp4 -o ./meeting-notes/

# Transcribe a tutorial with frequent screenshots
cc_transcribe tutorial.mp4 --threshold 0.85 --interval 0.5

# Quick transcription without images
cc_transcribe podcast.mp3 --no-screenshots

# Get video metadata
cc_transcribe video.mkv --info
```

---

## cc_gmail

Gmail CLI: read, send, search, and manage emails from the command line.
Supports **multiple Gmail accounts**.

**Requirements:**
- OAuth credentials from Google Cloud Console

### Setup

```bash
# 1. Add an account
cc_gmail accounts add personal

# 2. Follow setup instructions to get credentials.json from Google Cloud
# 3. Place credentials.json in ~/.cc_gmail/accounts/personal/
# 4. Authenticate
cc_gmail auth
```

See the [full README](https://github.com/CenterConsulting/cc_tools/tree/main/src/cc_gmail) for detailed Google Cloud setup steps.

### Multiple Accounts

```bash
# Add accounts
cc_gmail accounts add personal --default
cc_gmail accounts add work

# List accounts
cc_gmail accounts list

# Switch default
cc_gmail accounts default work

# Use specific account
cc_gmail --account work list
cc_gmail -a personal search "from:mom"
```

### Usage

```bash
# Authenticate
cc_gmail auth

# List inbox
cc_gmail list

# List sent messages
cc_gmail list -l SENT

# Show unread only
cc_gmail list --unread

# Read a specific email
cc_gmail read <message_id>

# Send email
cc_gmail send -t "recipient@example.com" -s "Subject" -b "Body text"

# Send with file body
cc_gmail send -t "recipient@example.com" -s "Subject" -f body.txt

# Send with attachments
cc_gmail send -t "to@example.com" -s "Subject" -b "See attached" -a file.pdf

# Create draft
cc_gmail draft -t "recipient@example.com" -s "Subject" -b "Draft body"

# Search emails
cc_gmail search "from:someone@example.com"
cc_gmail search "subject:important is:unread"

# List labels
cc_gmail labels

# Delete (move to trash)
cc_gmail delete <message_id>

# Show profile
cc_gmail profile
```

### Search Syntax

| Query | Description |
|-------|-------------|
| `from:email` | Messages from sender |
| `to:email` | Messages to recipient |
| `subject:word` | Subject contains word |
| `is:unread` | Unread messages |
| `has:attachment` | Has attachments |
| `after:YYYY/MM/DD` | After date |
| `before:YYYY/MM/DD` | Before date |

### Options

| Option | Description |
|--------|-------------|
| `-t, --to` | Recipient email |
| `-s, --subject` | Email subject |
| `-b, --body` | Email body text |
| `-f, --file` | Read body from file |
| `-l, --label` | Label/folder name |
| `-n, --count` | Number of results |
| `-a, --attach` | Attachment file |
| `--cc` | CC recipients |
| `--bcc` | BCC recipients |
| `--html` | Body is HTML |

---

## cc_outlook

Outlook CLI: read, send, search emails and manage calendar from the command line.
Supports **multiple Outlook accounts** (personal and work).

**Requirements:**
- Azure App Registration with OAuth credentials

### Setup

```bash
# 1. Create Azure App at https://portal.azure.com -> App registrations
# 2. Add redirect URIs: http://localhost AND https://login.microsoftonline.com/common/oauth2/nativeclient
# 3. Enable "Allow public client flows"
# 4. Add API permissions: Mail.ReadWrite, Mail.Send, Calendars.ReadWrite, User.Read

# Add account with your Client ID
cc_outlook accounts add your@email.com --client-id YOUR_CLIENT_ID

# Authenticate (browser opens, copy URL back when you see "not the right page")
cc_outlook auth
```

### Usage

```bash
# List inbox
cc_outlook list

# List sent/drafts/unread
cc_outlook list -f sent
cc_outlook list --unread

# Read email
cc_outlook read <message_id>

# Send email
cc_outlook send -t "to@example.com" -s "Subject" -b "Body text"

# Send with attachments
cc_outlook send -t "to@example.com" -s "Report" -b "See attached" --attach report.pdf

# Search
cc_outlook search "project update"

# Calendar events (next 7 days)
cc_outlook calendar events

# Calendar events (next 14 days)
cc_outlook calendar events -d 14

# Create calendar event
cc_outlook calendar create -s "Meeting" -d 2024-12-25 -t 14:00

# Show profile
cc_outlook profile

# Multiple accounts
cc_outlook accounts list
cc_outlook -a work list
```

---

## cc_youtube_info

Extract transcripts, metadata, chapters, and information from YouTube videos.

### Usage

```bash
# Get video metadata
cc_youtube_info info "https://www.youtube.com/watch?v=VIDEO_ID"

# Download transcript
cc_youtube_info transcript "https://www.youtube.com/watch?v=VIDEO_ID"

# Save transcript to file
cc_youtube_info transcript URL -o transcript.txt

# Download as SRT subtitles
cc_youtube_info transcript URL --format srt -o captions.srt

# List available languages
cc_youtube_info languages URL

# Get chapters
cc_youtube_info chapters URL

# Output as JSON
cc_youtube_info info URL --json
cc_youtube_info transcript URL --json
```

### Options

| Option | Description |
|--------|-------------|
| `-o, --output` | Output file path |
| `-l, --lang` | Language code (default: en) |
| `-f, --format` | Output format: txt, srt, vtt |
| `-p, --paragraphs` | Format as paragraphs (txt only) |
| `--json` | Output as JSON |
| `--auto-only` | Use only auto-generated captions |
| `--no-timestamps` | Remove timestamps (txt only) |

---

## cc_crawl4ai

AI-ready web crawler: crawl pages to clean markdown for LLM/RAG workflows.

### Usage

```bash
# Crawl a single URL
cc_crawl4ai crawl "https://example.com"

# Save to file
cc_crawl4ai crawl URL -o page.md

# Use fit markdown (noise filtered)
cc_crawl4ai crawl URL --fit

# Batch crawl from URL list
cc_crawl4ai batch urls.txt -o ./output/

# Stealth mode (evade bot detection)
cc_crawl4ai crawl URL --stealth

# Wait for dynamic content
cc_crawl4ai crawl URL --wait-for ".content-loaded"

# Scroll full page (for infinite scroll)
cc_crawl4ai crawl URL --scroll

# Extract specific CSS selector
cc_crawl4ai crawl URL --css "article.main"

# Take screenshot
cc_crawl4ai crawl URL --screenshot

# Session management (for authenticated crawling)
cc_crawl4ai session create mysite -u "https://example.com/login" --interactive
cc_crawl4ai crawl URL --session mysite
```

### Options

| Option | Description |
|--------|-------------|
| `-o, --output` | Output file path |
| `-f, --format` | Output format: markdown, json, html, raw |
| `--fit` | Use fit markdown (noise filtered) |
| `--stealth` | Enable stealth mode |
| `--wait-for` | CSS selector to wait for |
| `--scroll` | Scroll full page |
| `--css` | CSS selector for extraction |
| `--screenshot` | Capture screenshot |
| `-s, --session` | Use saved session |

---

## Installation

### Quick Install (Recommended)

Download and run the setup executable:

1. Download `cc_tools-setup-windows-x64.exe` from [GitHub Releases](https://github.com/CenterConsulting/cc_tools/releases)
2. Run it - it downloads tools, adds to PATH, installs this skill file
3. Restart your terminal

### Manual Install

Download individual tools from [GitHub Releases](https://github.com/CenterConsulting/cc_tools/releases):
- `cc_crawl4ai.exe`
- `cc_gmail.exe`
- `cc_markdown.exe`
- `cc_outlook.exe`
- `cc_transcribe.exe`
- `cc_youtube_info.exe`

Place in a directory in your PATH (e.g., `C:\cc_tools`).

---

## Requirements

- **cc_crawl4ai:** Playwright browsers (`playwright install chromium`)
- **cc_gmail:** OAuth credentials from Google Cloud Console
- **cc_markdown:** Chrome/Chromium for PDF generation (auto-detected)
- **cc_outlook:** Azure App Registration with OAuth credentials
- **cc_transcribe:** FFmpeg + OpenAI API key
- **cc_youtube_info:** No special requirements

Set API key:
```bash
# Windows
set OPENAI_API_KEY=your-key-here

# Linux/macOS
export OPENAI_API_KEY=your-key-here
```

---

## License

MIT License - https://github.com/CenterConsulting/cc_tools/blob/main/LICENSE
