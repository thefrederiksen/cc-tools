# cc_markdown

Convert Markdown to beautifully styled PDF, Word, and HTML documents.

**Requirement:** `cc_markdown.exe` must be in PATH

---

## Quick Reference

```bash
# Convert to PDF with theme
cc_markdown report.md -o report.pdf --theme boardroom

# Convert to Word
cc_markdown report.md -o report.docx

# Convert to HTML
cc_markdown report.md -o report.html

# List available themes
cc_markdown --themes
```

---

## Commands

### Basic Conversion

```bash
# PDF output
cc_markdown document.md -o document.pdf

# Word output
cc_markdown document.md -o document.docx

# HTML output
cc_markdown document.md -o document.html
```

### With Themes

```bash
# Corporate style
cc_markdown report.md -o report.pdf --theme boardroom

# Technical documentation
cc_markdown api-docs.md -o api-docs.pdf --theme blueprint

# Academic paper
cc_markdown thesis.md -o thesis.pdf --theme thesis

# Dark theme
cc_markdown notes.md -o notes.html --theme obsidian
```

### Custom CSS

```bash
# Use custom stylesheet
cc_markdown document.md -o output.pdf --css custom.css
```

### Page Settings

```bash
# Letter size paper
cc_markdown document.md -o output.pdf --page-size letter

# Custom margin
cc_markdown document.md -o output.pdf --margin 0.5in
```

---

## Available Themes

| Theme | Description | Best For |
|-------|-------------|----------|
| `paper` | Minimal, clean (default) | General documents |
| `boardroom` | Corporate, executive | Business reports |
| `terminal` | Technical, monospace | Code documentation |
| `blueprint` | Technical documentation | API docs, specs |
| `thesis` | Academic, scholarly | Papers, research |
| `spark` | Creative, colorful | Presentations |
| `obsidian` | Dark theme | Dark mode docs |

---

## Options

| Option | Description |
|--------|-------------|
| `-o, --output` | Output file path (format from extension) |
| `-t, --theme` | Built-in theme name |
| `--css` | Custom CSS file path |
| `--page-size` | Page size: a4, letter (default: a4) |
| `--margin` | Page margin (default: 1in) |
| `--themes` | List available themes |
| `-v, --version` | Show version |
| `--help` | Show help |

---

## Requirements

- Chrome/Chromium (for PDF generation)
- Automatically detected from common locations

---

## Examples

### Create a Business Report

```bash
cc_markdown quarterly-report.md -o report.pdf --theme boardroom
```

### Generate API Documentation

```bash
cc_markdown api-reference.md -o api-docs.pdf --theme blueprint --page-size letter
```

### Convert Meeting Notes

```bash
cc_markdown meeting-notes.md -o meeting-notes.docx --theme paper
```

### Create Dark Mode HTML

```bash
cc_markdown docs.md -o docs.html --theme obsidian
```

---

## LLM Use Cases

1. **Document conversion** - "Convert this markdown to PDF with corporate styling"
2. **Report generation** - "Create a PDF report from the analysis"
3. **Documentation** - "Generate API docs in PDF format"
4. **Academic papers** - "Format this paper using academic styling"
