# heyu-vault

Personal knowledge vault for systems, openEuler/Linux kernel learning, source reading, experiments, and long-term technical notes.

This repository is an Obsidian-first, Markdown-native knowledge base. It is designed to stay readable on GitHub, usable in Obsidian, and indexable by LLM tools.

## Start

1. Clone this repository.
2. Open it as an Obsidian vault.
3. Start from [START_HERE.md](START_HERE.md) or [00-Home.md](00-Home.md).
4. Capture rough material in `Inbox/` or `Daily/`.
5. Promote stable notes into concepts, labs, source reading, MOCs, or cheat sheets.

## Operating Model

- Notion tracks what to do.
- Obsidian stores what was learned.
- NoteLM/LLMNote indexes selected notes, docs, and source repositories.
- Codex helps inspect code, draft notes, and prepare contribution documents.

## Current Focus

- openEuler/Linux kernel knowledge system
- kernel source reading
- QEMU and build labs
- issue/PR analysis
- engineering cheat sheets

## Key Entry Points

- [START_HERE.md](START_HERE.md)
- [00-Home.md](00-Home.md)
- [Kernel MOC](MOCs/Kernel-MOC.md)
- [openEuler MOC](MOCs/openEuler-MOC.md)
- [Windows Knowledge Base Environment](07-CheatSheets/Windows-KB-Environment.md)
- [Private Policy](PRIVATE_POLICY.md)

## Local Tools

```powershell
python .\tools\check_vault.py
python .\tools\sync_kb_index.py
```

The human-readable index is generated at:

```text
indexes/kb-index.md
```

## Environment Setup

Windows setup for Obsidian, Notion, Scoop, and Git workflow is documented in:

[Windows Knowledge Base Environment](07-CheatSheets/Windows-KB-Environment.md)
