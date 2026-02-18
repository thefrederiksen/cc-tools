# cc_youtube_info

Extract transcripts, metadata, chapters, and information from YouTube videos.

**Requirement:** `cc_youtube_info.exe` must be in PATH

---

## Quick Reference

```bash
# Get video metadata
cc_youtube_info info "https://www.youtube.com/watch?v=VIDEO_ID"

# Download transcript
cc_youtube_info transcript URL -o transcript.txt

# List available languages
cc_youtube_info languages URL

# Get chapters
cc_youtube_info chapters URL
```

---

## Commands

### Video Info

```bash
# Display video metadata
cc_youtube_info info URL

# Output as JSON
cc_youtube_info info URL --json
```

Shows: title, channel, duration, views, likes, comments, upload date, captions availability, chapters

### Transcript

```bash
# Print transcript to console
cc_youtube_info transcript URL

# Save to file
cc_youtube_info transcript URL -o transcript.txt

# Specific language
cc_youtube_info transcript URL --lang es

# Format as SRT subtitles
cc_youtube_info transcript URL --format srt -o captions.srt

# Format as VTT subtitles
cc_youtube_info transcript URL --format vtt -o captions.vtt

# Without timestamps
cc_youtube_info transcript URL --no-timestamps

# As paragraphs (grouped text)
cc_youtube_info transcript URL --paragraphs

# Output as JSON with metadata
cc_youtube_info transcript URL --json

# Use only auto-generated captions
cc_youtube_info transcript URL --auto-only
```

### Languages

```bash
# List available caption languages
cc_youtube_info languages URL

# Output as JSON
cc_youtube_info languages URL --json
```

### Chapters

```bash
# List video chapters with timestamps
cc_youtube_info chapters URL

# Output as JSON
cc_youtube_info chapters URL --json
```

---

## Options

| Option | Description |
|--------|-------------|
| `-o, --output` | Output file path |
| `-l, --lang` | Language code (default: en) |
| `-f, --format` | Output format: txt, srt, vtt |
| `-p, --paragraphs` | Format as paragraphs (txt only) |
| `-j, --json` | Output as JSON |
| `--auto-only` | Use only auto-generated captions |
| `--no-timestamps` | Remove timestamps (txt only) |
| `-v, --version` | Show version |

---

## URL Formats

All of these work:
- `https://www.youtube.com/watch?v=VIDEO_ID`
- `https://youtu.be/VIDEO_ID`
- `https://www.youtube.com/embed/VIDEO_ID`
- Just the video ID: `VIDEO_ID`

---

## Examples

### Get Video Summary

```bash
cc_youtube_info info "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

Output:
```
+------------------+----------------------------+
| Property         | Value                      |
+------------------+----------------------------+
| Title            | Never Gonna Give You Up    |
| Channel          | Rick Astley                |
| Duration         | 3:33                       |
| Views            | 1,500,000,000              |
| Likes            | 15,000,000                 |
| Manual Captions  | Yes                        |
| Auto Captions    | Yes                        |
+------------------+----------------------------+
```

### Download Transcript for Analysis

```bash
cc_youtube_info transcript URL -o transcript.txt
```

### Get Spanish Transcript

```bash
cc_youtube_info transcript URL --lang es -o spanish.txt
```

### Create SRT Subtitles

```bash
cc_youtube_info transcript URL --format srt -o subtitles.srt
```

### Check What Languages Are Available

```bash
cc_youtube_info languages URL
```

Output:
```
Available Languages:
  en: English
  en (auto-generated): English (auto-generated)
  es: Spanish
  de: German
```

### Get Chapter Breakdown

```bash
cc_youtube_info chapters URL
```

Output:
```
Chapters (5):
  0:00  Introduction
  2:15  Getting Started
  8:30  Main Content
  15:45 Advanced Tips
  22:00 Conclusion
```

---

## LLM Use Cases

1. **Video summarization** - "Get the transcript from this YouTube video and summarize it"
2. **Research** - "Extract metadata and transcript for this video"
3. **Content analysis** - "What are the chapters in this video?"
4. **Translation prep** - "Download the English transcript so I can translate it"
5. **Accessibility** - "Create SRT subtitles from this video"
