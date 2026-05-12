---
type: output
module: openeuler
status: seed
created: 2026-05-12
updated: 2026-05-12
source:
tags:
  - ai-memory
  - decisions
  - workflow
---

# Project Decisions

This note records durable decisions for the vault.

## Decisions

| Date | Decision | Reason |
| --- | --- | --- |
| 2026-05-12 | Obsidian Markdown is the source of truth. | Keeps the vault local-first, Git-friendly, and portable. |
| 2026-05-12 | Notion stores task state only. | Avoids duplicating long-form knowledge across tools. |
| 2026-05-12 | AI writes drafts first, not unreviewed long-term notes. | Prevents temporary assumptions from becoming permanent rules. |
| 2026-05-12 | Track Markdown indexes, ignore JSON indexes. | Markdown is useful on GitHub; JSON is generated tooling output. |
| 2026-05-12 | Keep a smaller LLM index. | Reduces retrieval noise and token usage. |

## Open Questions

- Whether to publish part of this vault with MkDocs or Quartz later.
- Whether to add a public/private split if the vault grows beyond technical notes.
