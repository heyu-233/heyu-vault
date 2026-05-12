---
type: concept
module: openeuler
status: seed
created: 2026-05-12
updated: 2026-05-12
source:
tags:
  - ai-memory
  - codex
  - workflow
---

# AI Operating Rules

This note records durable rules for AI-assisted work in this vault.

## Source of Truth

- Obsidian Markdown files are the long-term knowledge source.
- Notion stores task state only.
- AI may draft, index, summarize, and propose edits.
- Confirmed notes should be reviewed before they become long-term knowledge.

## Before Editing

- Read `START_HERE.md`, `00-Home.md`, and `indexes/llm-index.md` when context is missing.
- Prefer existing templates and folder conventions.
- Keep generated notes in `Drafts/` until they are reviewed.

## Before Commit

Run:

```powershell
python .\tools\check_vault.py
python .\tools\sync_kb_index.py
python .\tools\sync_kb_index.py --profile llm
git status --short
```

Do not commit `.obsidian/`, generated JSON indexes, private attachments, resumes, tokens, or large binaries.

## Indexing Rule

- `indexes/kb-index.md` is the full human-readable index.
- `indexes/llm-index.md` is the smaller AI retrieval index.
- `Inbox/`, `Daily/`, `Drafts/`, `Templates/`, attachments, and generated indexes should stay out of the LLM index by default.
