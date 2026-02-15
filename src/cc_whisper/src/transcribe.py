"""Audio transcription using OpenAI Whisper API."""

import os
from pathlib import Path
from typing import Optional

from openai import OpenAI


def get_api_key() -> str:
    """Get OpenAI API key from environment."""
    key = os.environ.get("OPENAI_API_KEY")
    if not key:
        raise RuntimeError("OPENAI_API_KEY environment variable not set")
    return key


def transcribe(
    audio_path: Path,
    language: Optional[str] = None,
    timestamps: bool = False,
) -> dict:
    """
    Transcribe audio file.

    Args:
        audio_path: Path to audio file
        language: Language code (e.g., "en", "es") or None for auto-detect
        timestamps: Include word-level timestamps

    Returns:
        Dict with 'text' and optionally 'words' and 'segments'
    """
    audio_path = Path(audio_path)
    if not audio_path.exists():
        raise FileNotFoundError(f"Audio file not found: {audio_path}")

    client = OpenAI(api_key=get_api_key())

    with open(audio_path, "rb") as f:
        kwargs = {
            "model": "whisper-1",
            "file": f,
        }

        if language:
            kwargs["language"] = language

        if timestamps:
            kwargs["response_format"] = "verbose_json"
            kwargs["timestamp_granularities"] = ["word", "segment"]

        response = client.audio.transcriptions.create(**kwargs)

    if timestamps:
        words = []
        if hasattr(response, "words") and response.words:
            for w in response.words:
                words.append({
                    "word": w.word,
                    "start": w.start,
                    "end": w.end,
                })

        segments = []
        if hasattr(response, "segments") and response.segments:
            for s in response.segments:
                segments.append({
                    "start": s.start,
                    "end": s.end,
                    "text": s.text.strip(),
                })

        return {
            "text": response.text,
            "words": words,
            "segments": segments,
            "duration": getattr(response, "duration", 0.0),
        }

    return {"text": response.text}


def transcribe_to_file(
    audio_path: Path,
    output_path: Path,
    language: Optional[str] = None,
    timestamps: bool = False,
) -> Path:
    """Transcribe audio and save to file."""
    result = transcribe(audio_path, language, timestamps)

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    if timestamps and result.get("segments"):
        # Format with timestamps
        lines = []
        for seg in result["segments"]:
            start = seg["start"]
            mins = int(start // 60)
            secs = int(start % 60)
            lines.append(f"[{mins:02d}:{secs:02d}] {seg['text']}")
        output_path.write_text("\n".join(lines), encoding="utf-8")
    else:
        output_path.write_text(result["text"], encoding="utf-8")

    return output_path
