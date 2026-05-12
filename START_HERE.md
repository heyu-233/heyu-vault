---
type: index
module: openeuler
status: seed
created: 2026-05-12
updated: 2026-05-12
source:
tags:
  - start
  - workflow
  - obsidian
---

# START HERE

This vault is a personal technical knowledge base. It currently focuses on openEuler/Linux kernel learning, but the structure is intended to grow into a broader engineering vault.

## 5-Minute Start

1. Open this folder as an Obsidian vault.
2. Open [[00-Home|00-Home]].
3. If you are capturing rough material, write it in [[Inbox/README|Inbox]].
4. If you are recording today's work, write it in [[Daily/README|Daily]].
5. If the note is stable, promote it into a concept, lab, source reading note, MOC, or cheat sheet.

## Daily Use

```text
Capture -> Daily/Inbox
Clarify -> Templates
Connect -> MOCs and related notes
Consolidate -> Concepts/Labs/CheatSheets
Publish -> Outputs
```

## Where Things Go

| Need | Put it here |
| --- | --- |
| Temporary idea, link, quote | `Inbox/` |
| Daily work log | `Daily/` |
| Kernel concept | `02-Kernel-Concepts/` |
| Code reading | `04-Source-Reading/` |
| Reproducible experiment | `05-Labs/` |
| Issue or PR analysis | `06-Issues-PRs/` |
| Commands and troubleshooting | `07-CheatSheets/` |
| Blog/resume/interview material | `08-Outputs/` |
| Topic navigation | `MOCs/` |
| Images and small public files | `Attachments/` |

## Maintenance Commands

```powershell
python .\tools\check_vault.py
python .\tools\sync_kb_index.py
```

## Safety

Read [[PRIVATE_POLICY|PRIVATE POLICY]] before committing personal files, screenshots, or attachments.
