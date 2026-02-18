# cc_vault Skill

Interact with the Vault 2.0 personal data platform. Import documents, ask questions, manage contacts/tasks/goals/ideas.

## Triggers

- `/vault`
- `vault ask`
- `vault import`
- `search vault`
- `add to vault`

## Tool Location

`C:\cc-tools\cc_vault.exe`

## Quick Reference

### Main Commands

```bash
# Initialize vault
cc_vault init

# Get stats
cc_vault stats

# Ask a question (RAG)
cc_vault ask "What tasks do I have this week?"

# Search
cc_vault search "project requirements"
cc_vault search "project requirements" --hybrid
```

### Tasks

```bash
# List tasks
cc_vault tasks list
cc_vault tasks list -s completed
cc_vault tasks list -s all

# Add task
cc_vault tasks add "Task title" -d 2026-02-25 -p high

# Complete/cancel task
cc_vault tasks done 1
cc_vault tasks cancel 2
```

### Goals

```bash
# List goals
cc_vault goals list
cc_vault goals list -s achieved

# Add goal
cc_vault goals add "Goal title" -t 2026-03-01

# Update goal
cc_vault goals progress 1 75
cc_vault goals achieve 1
cc_vault goals pause 1
cc_vault goals resume 1
```

### Ideas

```bash
# List ideas
cc_vault ideas list
cc_vault ideas list -s actionable

# Add idea
cc_vault ideas add "New idea" -c product

# Update idea status
cc_vault ideas actionable 1
cc_vault ideas archive 1
```

### Contacts

```bash
# List contacts
cc_vault contacts list
cc_vault contacts list -s "john"

# Add contact
cc_vault contacts add "John Doe" -e john@example.com -c "Acme Corp"

# Show contact
cc_vault contacts show 1

# Add memory
cc_vault contacts memory 1 "Prefers morning meetings"

# Update contact
cc_vault contacts update 1 -r "VP Sales"
```

### Documents

```bash
# List documents
cc_vault docs list
cc_vault docs list -t research

# Import document (PDF, Word, Markdown, text)
cc_vault docs add document.pdf -t research
cc_vault docs add notes.md -t note --title "Meeting Notes"

# Show document
cc_vault docs show 1

# Search documents (FTS)
cc_vault docs search "keyword"
```

### Health

```bash
# List health entries
cc_vault health list
cc_vault health list -c daily -d 30

# Get AI insights
cc_vault health insights -q "sleep patterns"
```

### Configuration

```bash
# Show config
cc_vault config show

# Set config
cc_vault config set vault_path D:\Vault
```

## Environment Variables

- `CC_VAULT_PATH`: Vault directory path (default: ~/Vault)
- `OPENAI_API_KEY`: Required for RAG features

## Notes

- RAG queries require OPENAI_API_KEY to be set
- Document import supports .docx, .pdf, .md, .txt
- Vector search requires chromadb (installed with [full] dependencies)
- Hybrid search combines vector similarity + BM25 keyword matching
