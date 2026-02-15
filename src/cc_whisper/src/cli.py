"""CLI for cc_whisper."""

import json
from pathlib import Path
from typing import Optional

import typer
from rich.console import Console

try:
    from . import __version__
    from .transcribe import transcribe, transcribe_to_file
except ImportError:
    from src import __version__
    from src.transcribe import transcribe, transcribe_to_file

app = typer.Typer(
    name="cc_whisper",
    help="Transcribe audio files using OpenAI Whisper.",
    add_completion=False,
)
console = Console()


def version_callback(value: bool):
    if value:
        console.print(f"cc_whisper version {__version__}")
        raise typer.Exit()


@app.command()
def main(
    audio: Path = typer.Argument(..., help="Audio file to transcribe", exists=True),
    output: Optional[Path] = typer.Option(None, "-o", "--output", help="Output file (default: print to console)"),
    language: Optional[str] = typer.Option(None, "-l", "--language", help="Language code (e.g., en, es, de)"),
    timestamps: bool = typer.Option(False, "-t", "--timestamps", help="Include timestamps"),
    json_output: bool = typer.Option(False, "--json", help="Output as JSON"),
    version: bool = typer.Option(
        False, "--version", "-v",
        callback=version_callback,
        is_eager=True,
        help="Show version",
    ),
):
    """Transcribe audio using OpenAI Whisper."""

    size_mb = audio.stat().st_size / 1024 / 1024
    console.print(f"[blue]Audio:[/blue] {audio.name} ({size_mb:.1f} MB)")

    if language:
        console.print(f"[blue]Language:[/blue] {language}")

    try:
        console.print("[blue]Transcribing...[/blue]")

        if output:
            if json_output:
                result = transcribe(audio, language, timestamps)
                output.parent.mkdir(parents=True, exist_ok=True)
                output.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
            else:
                transcribe_to_file(audio, output, language, timestamps)

            console.print(f"[green]Saved:[/green] {output}")
        else:
            result = transcribe(audio, language, timestamps)

            if json_output:
                console.print(json.dumps(result, indent=2, ensure_ascii=False))
            elif timestamps and result.get("segments"):
                for seg in result["segments"]:
                    start = seg["start"]
                    mins = int(start // 60)
                    secs = int(start % 60)
                    console.print(f"[cyan][{mins:02d}:{secs:02d}][/cyan] {seg['text']}")
            else:
                console.print(result["text"])

    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")
        raise typer.Exit(1)


if __name__ == "__main__":
    app()
