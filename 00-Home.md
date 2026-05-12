---
type: index
module: openeuler
status: seed
created: 2026-05-11
updated: 2026-05-11
source:
tags:
  - openeuler
  - kernel
  - knowledge-base
---

# openEuler Kernel Lab

这个 vault 是 openEuler/Linux 内核知识体系的事实源。

## Today

如果只是想开始记录，不要纠结分类：

1. 临时想法、网页摘录、未整理材料：写到 [[Inbox/README|Inbox]]。
2. 今天学了什么、做了什么、卡在哪里：写到 [[Daily/README|Daily]]。
3. 已经清晰的知识：迁移到 Concepts、Labs、Source Reading、CheatSheets 或 MOCs。
4. 每周整理一次，把 Daily/Inbox 中有价值的内容提升为正式笔记。

## Main Maps

- [[MOCs/Kernel-MOC|Kernel MOC]]
- [[MOCs/openEuler-MOC|openEuler MOC]]
- [[MOCs/Embedded-Linux-MOC|Embedded Linux MOC]]
- [[MOCs/Rust-MOC|Rust MOC]]

## Templates

- [[Templates/Daily|Daily Template]]
- [[Templates/Inbox|Inbox Template]]
- [[Templates/Concept|Concept Template]]
- [[Templates/Source-Reading|Source Reading Template]]
- [[Templates/Lab|Lab Template]]
- [[Templates/Issue|Issue Template]]
- [[Templates/CheatSheet|CheatSheet Template]]

## Operating Model

- Notion 负责我要做什么：任务看板、路线图、进度和下一步。
- Obsidian 负责我学到了什么：概念、源码阅读、实验、问题复盘和输出。
- NoteLM/LLMNote 负责我怎么快速问资料：索引 vault、源码、官方文档和 issue。
- Codex 负责我怎么推进代码和文档：源码导览、实验脚本、笔记整理、PR 文档草稿。

## Start Here

- [[START_HERE|START HERE]]
- [[01-Roadmap/Kernel-Learning-Roadmap|Kernel Learning Roadmap]]
- [[03-openEuler/openEuler-Kernel|openEuler Kernel]]
- [[04-Source-Reading/Kernel-Source-Map|Kernel Source Map]]
- [[05-Labs/QEMU-Boot-openEuler|QEMU Boot openEuler]]
- [[06-Issues-PRs/Candidate-Issues|Candidate Issues]]
- [[07-CheatSheets/Kernel-Build-Commands|Kernel Build Commands]]
- [[99-Refs/Links|Links]]

## Current Focus

- Build a stable openEuler kernel learning map.
- Run at least one QEMU/openEuler kernel experiment.
- Keep issue analysis tied to kernel concepts and source reading.
- Convert useful notes into blog drafts, PR notes, and resume material.

## Notion Dashboard Fields

Use one Notion database named `openEuler Kernel Lab` with these fields:

| Field | Values |
| --- | --- |
| Name | Task title |
| Type | Learning, Source Reading, Lab, Issue, PR, Output |
| Module | Boot, Scheduler, Memory, Driver, Network, Filesystem, Debugging, openEuler |
| Status | Backlog, Doing, Blocked, Review, Done |
| Priority | P0, P1, P2 |
| Obsidian Path | Relative path to this vault |
| Repo/Issue URL | Source, issue, PR, or doc link |
| Next Action | One concrete next action |
| Due Date | Optional |
| Updated At | Last update date |

## Rules

- Obsidian is the source of truth for long-form knowledge.
- Notion stores status only; do not duplicate full notes there.
- LLM tools may suggest edits, but confirmed notes live in Markdown.
- Every experiment should record commands, environment, result, and follow-ups.
