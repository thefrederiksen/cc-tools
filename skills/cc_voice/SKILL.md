# cc_voice

Convert text to speech using OpenAI TTS.

**Requirements:**
- `cc_voice.exe` must be in PATH
- OpenAI API key: set `OPENAI_API_KEY` environment variable

---

## Quick Reference

```bash
# Convert text to speech
cc_voice "Hello, this is a test" -o hello.mp3

# Use different voice
cc_voice "Welcome to the show" -o welcome.mp3 --voice nova

# Read from file
cc_voice notes.txt -o notes.mp3

# High definition model
cc_voice "Important announcement" -o announcement.mp3 --model tts-1-hd
```

---

## Commands

### Basic Text-to-Speech

```bash
# Convert text string
cc_voice "Your text here" -o output.mp3

# Read text from file
cc_voice document.txt -o document.mp3
cc_voice README.md -o readme.mp3
```

### Voice Selection

```bash
# Alloy - neutral, balanced
cc_voice "text" -o out.mp3 --voice alloy

# Echo - male, warm
cc_voice "text" -o out.mp3 --voice echo

# Fable - British accent
cc_voice "text" -o out.mp3 --voice fable

# Nova - female, friendly
cc_voice "text" -o out.mp3 --voice nova

# Onyx - male, deep (default)
cc_voice "text" -o out.mp3 --voice onyx

# Shimmer - female, expressive
cc_voice "text" -o out.mp3 --voice shimmer
```

### Quality Settings

```bash
# Standard quality (faster, cheaper)
cc_voice "text" -o out.mp3 --model tts-1

# High definition (better quality)
cc_voice "text" -o out.mp3 --model tts-1-hd
```

### Speed Control

```bash
# Normal speed (1.0)
cc_voice "text" -o out.mp3 --speed 1.0

# Slower (0.5x)
cc_voice "text" -o out.mp3 --speed 0.5

# Faster (1.5x)
cc_voice "text" -o out.mp3 --speed 1.5

# Maximum speed (4.0x)
cc_voice "text" -o out.mp3 --speed 4.0
```

### Raw Output

```bash
# Skip markdown cleaning (for plain text)
cc_voice "text" -o out.mp3 --raw
```

---

## Options

| Option | Description |
|--------|-------------|
| `-o, --output` | Output audio file path (required) |
| `-v, --voice` | Voice: alloy, echo, fable, nova, onyx, shimmer |
| `-m, --model` | Model: tts-1, tts-1-hd |
| `-s, --speed` | Speed: 0.25 to 4.0 (default: 1.0) |
| `--raw` | Don't clean markdown formatting |
| `--version` | Show version |

---

## Available Voices

| Voice | Description | Best For |
|-------|-------------|----------|
| `alloy` | Neutral, balanced | General purpose |
| `echo` | Male, warm | Narration |
| `fable` | British accent | Storytelling |
| `nova` | Female, friendly | Customer service |
| `onyx` | Male, deep | Announcements |
| `shimmer` | Female, expressive | Engaging content |

---

## Examples

### Create Audio from Notes

```bash
cc_voice meeting-notes.md -o meeting-notes.mp3 --voice nova
```

### Generate Announcement

```bash
cc_voice "Attention: The system will be under maintenance tonight at 10 PM." \
  -o announcement.mp3 --voice onyx --model tts-1-hd
```

### Create Audiobook Chapter

```bash
cc_voice chapter1.txt -o chapter1.mp3 --voice fable --speed 0.9
```

### Quick Voice Memo

```bash
cc_voice "Remember to call John tomorrow at 3 PM" -o reminder.mp3
```

---

## Tips

1. **Markdown files** - The tool automatically cleans markdown formatting for natural speech
2. **Long text** - Works with text files of any length
3. **Cost optimization** - Use `tts-1` for drafts, `tts-1-hd` for final versions
4. **Speed adjustment** - Slower speeds (0.8-0.9) often sound more natural for narration

---

## LLM Use Cases

1. **Text-to-speech** - "Convert this document to an audio file"
2. **Narration** - "Create an audio version of this article"
3. **Announcements** - "Generate an audio announcement for this message"
4. **Accessibility** - "Create an audio file of this README"
5. **Voice memos** - "Read this note aloud and save as MP3"
