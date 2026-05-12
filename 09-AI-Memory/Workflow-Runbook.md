---
type: cheatsheet
module: openeuler
status: seed
created: 2026-05-12
updated: 2026-05-12
source:
tags:
  - ai-memory
  - runbook
  - workflow
---

# Workflow Runbook

Use this as the standard operating flow for AI-assisted vault work.

## Start A New Session

1. Read `START_HERE.md`.
2. Read `indexes/llm-index.md`.
3. Read relevant MOC files.
4. Read relevant files from `09-AI-Memory/`.

## Batch Knowledge Import

1. Put raw material in `Inbox/`.
2. Ask AI to extract candidate notes into `Drafts/`.
3. Review and correct the drafts.
4. Promote stable notes into formal folders.
5. Link promoted notes from MOCs.
6. Regenerate indexes and run checks.

## Commands

```powershell
python .\tools\check_vault.py
python .\tools\sync_kb_index.py
python .\tools\sync_kb_index.py --profile llm
git status --short
```

## Commit Flow

```powershell
git add .
git commit -m "Update vault notes"
git push
```

Before committing, confirm that `.obsidian/`, `indexes/*.json`, and private attachments are still ignored.
