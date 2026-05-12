---
type: cheatsheet
module: openeuler
status: seed
created: 2026-05-11
updated: 2026-05-11
source:
tags:
  - llm
  - indexing
  - notelm
---

# LLM Indexing

## First Index Set

Index only focused sources:

1. `MOCs/`
2. `02-Kernel-Concepts/`
3. `04-Source-Reading/`
4. `05-Labs/`
5. `07-CheatSheets/`
6. openEuler kernel repository when cloned
7. Linux kernel `Documentation/`
8. openEuler official docs used by current labs
9. Issue and PR notes created in this vault

Do not index the whole openEuler organization in the first pass.

## Default Exclusions

- Do not index `Inbox/` by default. It contains rough and noisy material.
- Do not index `Daily/` by default unless a note has been cleaned or promoted.
- Do not index `Attachments/private/`.
- Do not index `.obsidian/`.

## Useful Questions

- Which notes explain QEMU boot for openEuler?
- Which kernel files should I inspect for scheduler basics?
- Which issue notes mention procfs or sysfs?
- What did I learn from the last lab?
- Which notes are mature enough to become a blog draft?

## Safety Rule

LLM tools may answer, summarize, and draft. They should not directly rewrite confirmed vault notes without review.

## Index Files

Generate local index files with:

```powershell
python .\tools\sync_kb_index.py
```

Generate a smaller LLM-oriented index with:

```powershell
python .\tools\sync_kb_index.py --profile llm
```

Use `indexes/kb-index.md` for human review and `indexes/kb-index.json` for tool integration.
Use `indexes/llm-index.md` when a retrieval tool should avoid `Inbox/`, `Daily/`, templates, attachments, and generated indexes.
