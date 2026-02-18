# cc_whisper

Transcribe audio files using OpenAI Whisper.

**Requirements:**
- `cc_whisper.exe` must be in PATH
- OpenAI API key: set `OPENAI_API_KEY` environment variable

---

## Quick Reference

```bash
# Transcribe audio
cc_whisper audio.mp3

# Save to file
cc_whisper audio.mp3 -o transcript.txt

# With timestamps
cc_whisper audio.mp3 --timestamps

# Output as JSON
cc_whisper audio.mp3 --json
```

---

## Commands

### Basic Transcription

```bash
# Transcribe and print to console
cc_whisper recording.mp3

# Save to file
cc_whisper recording.mp3 -o transcript.txt

# Specify language
cc_whisper recording.mp3 --language en
cc_whisper recording.mp3 --language es
cc_whisper recording.mp3 --language de
```

### With Timestamps

```bash
# Include timestamps in output
cc_whisper meeting.mp3 --timestamps
```

Output:
```
[00:00] Hello everyone, welcome to the meeting.
[00:05] Let's start with the agenda.
[00:12] First item is the quarterly review.
```

### JSON Output

```bash
# Output as JSON (to console)
cc_whisper audio.mp3 --json

# Save JSON to file
cc_whisper audio.mp3 --json -o transcript.json
```

JSON structure:
```json
{
  "text": "Full transcript text...",
  "segments": [
    {
      "start": 0.0,
      "end": 3.5,
      "text": "Hello everyone"
    }
  ]
}
```

---

## Options

| Option | Description |
|--------|-------------|
| `-o, --output` | Output file path |
| `-l, --language` | Language code (e.g., en, es, de, fr) |
| `-t, --timestamps` | Include timestamps |
| `--json` | Output as JSON |
| `-v, --version` | Show version |

---

## Supported Audio Formats

| Format | Extension |
|--------|-----------|
| MP3 | .mp3 |
| WAV | .wav |
| M4A | .m4a |
| FLAC | .flac |
| OGG | .ogg |
| WebM | .webm |

---

## Examples

### Transcribe a Podcast

```bash
cc_whisper podcast-episode.mp3 -o episode-transcript.txt
```

### Meeting Notes with Timestamps

```bash
cc_whisper meeting-recording.m4a --timestamps -o meeting-notes.txt
```

Output:
```
[00:00] Welcome everyone to today's standup.
[00:15] Sarah, would you like to start?
[01:23] Thanks. Yesterday I completed the API integration.
```

### Spanish Audio

```bash
cc_whisper spanish-interview.mp3 --language es -o interview.txt
```

### JSON for Further Processing

```bash
cc_whisper lecture.mp3 --json -o lecture.json
```

---

## Language Codes

Common language codes:
- `en` - English
- `es` - Spanish
- `de` - German
- `fr` - French
- `it` - Italian
- `pt` - Portuguese
- `zh` - Chinese
- `ja` - Japanese
- `ko` - Korean

Whisper auto-detects language if not specified.

---

## Tips

1. **Auto-detection** - If you don't specify a language, Whisper will auto-detect it
2. **File size** - Large files may take longer; consider extracting audio from video first
3. **Quality** - Better audio quality = better transcription accuracy
4. **Timestamps** - Use `--timestamps` for meeting notes where you need to reference times

---

## LLM Use Cases

1. **Transcription** - "Transcribe this audio recording"
2. **Meeting notes** - "Create a transcript of this meeting with timestamps"
3. **Podcast processing** - "Convert this podcast to text"
4. **Multilingual** - "Transcribe this Spanish audio file"
5. **Data extraction** - "Get the JSON transcript for processing"
