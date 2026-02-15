# CC Tools

Open source CLI tools for agentic coding workflows. Download. Run. Done.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://github.com/CenterConsulting/cc-tools/workflows/Build/badge.svg)](https://github.com/CenterConsulting/cc-tools/actions)

---

## Quick Install

### Windows (Recommended)

Download and run the setup executable:

1. Download **[cc-tools-setup-windows-x64.exe](../../releases/latest)** from GitHub Releases
2. Double-click to run
3. Restart your terminal

The setup will:
- Download all available cc-tools to `%LOCALAPPDATA%\cc-tools\`
- Add to your PATH
- Install SKILL.md for Claude Code integration

### Alternative: Individual Downloads

Download specific tools from [GitHub Releases](../../releases):
- `cc_markdown-windows-x64.exe`
- `cc_transcribe-windows-x64.exe`
- *(more coming soon)*

Place in any directory in your PATH.

---

## What is CC Tools?

CC Tools is a suite of command-line utilities designed for AI-assisted development workflows. Each tool is a single executable - no installation, no dependencies, just download and run.

Built by [CenterConsulting Inc.](https://www.centerconsulting.com) and released under the MIT license.

---

## Tools

| Tool | Description | Status |
|------|-------------|--------|
| **cc_markdown** | Markdown to PDF/Word/HTML with themes | Available |
| **cc_transcribe** | Video/audio transcription with timestamps | In Development |
| **cc_image** | Image toolkit: generate, analyze, OCR, resize, convert | Coming Soon |
| **cc_voice** | Text-to-speech | Coming Soon |
| **cc_whisper** | Audio transcription | Coming Soon |
| **cc_video** | Video utilities | Coming Soon |

---

## Quick Start

### cc_markdown

Convert Markdown to beautifully styled documents:

```bash
# PDF with corporate theme
cc_markdown report.md -o report.pdf --theme boardroom

# Word document
cc_markdown report.md -o report.docx --theme paper

# HTML
cc_markdown report.md -o report.html

# Custom CSS
cc_markdown report.md -o report.pdf --css custom.css

# List themes
cc_markdown --themes
```

**Built-in Themes:**
- **boardroom** - Corporate, executive
- **terminal** - Technical, monospace
- **paper** - Minimal, elegant
- **spark** - Creative, colorful
- **thesis** - Academic, scholarly
- **obsidian** - Dark theme
- **blueprint** - Technical docs

### cc_transcribe

Transcribe video/audio with timestamps and screenshots:

```bash
# Basic transcription
cc_transcribe video.mp4

# Specify output directory
cc_transcribe video.mp4 -o ./output/

# Without screenshots
cc_transcribe video.mp4 --no-screenshots
```

Requires FFmpeg and `OPENAI_API_KEY` environment variable.

---

## Installation Details

### What Gets Installed

| File | Location | Purpose |
|------|----------|---------|
| `cc_*.exe` | `%LOCALAPPDATA%\cc-tools\` | The CLI tools |
| `SKILL.md` | `~/.claude/skills/cc-tools/` | Claude Code integration |

### Updating

Run `cc-tools-setup.exe` again to download the latest versions.

### Build from Source

```bash
# Clone the repo
git clone https://github.com/CenterConsulting/cc-tools.git
cd cc-tools

# Build all tools
scripts\build-all.bat

# Or build individual tools
scripts\build-setup.bat
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed build instructions.

---

## Why CC Tools?

**For Agentic Workflows:** Simple CLI interfaces that AI coding assistants can call directly.

**MIT Licensed:** Use anywhere - personal, commercial, no restrictions.

**Single Executables:** No runtime dependencies. Download and run.

**Modular:** Each tool is independent. Download only what you need.

---

## Documentation

- [Implementation Plan](docs/IMPLEMENTATION_PLAN.md)
- [Strategy Document](docs/CC_Tools_Strategy.md)
- [cc_markdown PRD](docs/cc_markdown_PRD.md)
- [Handover Document](docs/HANDOVER.md)

---

## Requirements

Some tools require an OpenAI API key for AI features:

```bash
# Windows
set OPENAI_API_KEY=your-key-here

# Linux/macOS
export OPENAI_API_KEY=your-key-here
```

Note: Some features (like cc_markdown) work without an API key.

---

## Contributing

Contributions welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## License

MIT License - see [LICENSE](LICENSE)

---

## About

Built by [CenterConsulting Inc.](https://www.centerconsulting.com)

We build AI-powered tools for process mining, document automation, and business intelligence.
