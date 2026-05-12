---
type: index
module: openeuler
status: seed
created: 2026-05-12
updated: 2026-05-12
source:
tags:
  - drafts
  - ai
  - workflow
---

# Drafts

Use this folder for AI-assisted candidate notes before they become long-term knowledge.

## Flow

```text
Inbox/ -> Drafts/ -> confirmed vault folders
```

## What Belongs Here

- AI-generated summaries from raw notes, links, issues, PRs, or source-reading sessions.
- Candidate notes that still need human review.
- Batch-cleaned notes before they are promoted into concepts, labs, source reading, MOCs, or cheat sheets.

## Promotion Rule

Before moving a draft into a formal folder:

1. Check facts and commands.
2. Remove private material.
3. Add stable frontmatter.
4. Link it from the relevant MOC or source note.
5. Run the vault checks.

```powershell
python .\tools\check_vault.py
python .\tools\sync_kb_index.py
python .\tools\sync_kb_index.py --profile llm
```
