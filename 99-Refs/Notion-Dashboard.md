---
type: cheatsheet
module: openeuler
status: seed
created: 2026-05-11
updated: 2026-05-11
source:
tags:
  - notion
  - workflow
---

# Notion Dashboard

Create one Notion database named `openEuler Kernel Lab`.

## Fields

| Field | Type | Values |
| --- | --- | --- |
| Name | Title | Task title |
| Type | Select | Learning, Source Reading, Lab, Issue, PR, Output |
| Module | Select | Boot, Scheduler, Memory, Driver, Network, Filesystem, Debugging, openEuler |
| Status | Select | Backlog, Doing, Blocked, Review, Done |
| Priority | Select | P0, P1, P2 |
| Obsidian Path | Text | Relative vault path |
| Repo/Issue URL | URL | Source, issue, PR, or docs |
| Next Action | Text | One concrete next step |
| Due Date | Date | Optional |
| Updated At | Date | Last update |

## Rule

Notion stores state only. Full notes stay in Obsidian.

## Starter Rows

| Name | Type | Module | Status | Priority | Obsidian Path | Next Action |
| --- | --- | --- | --- | --- | --- | --- |
| Build openEuler Kernel | Lab | openEuler | Backlog | P1 | `05-Labs/Build-openEuler-Kernel.md` | Confirm branch and build environment |
| QEMU Boot openEuler | Lab | Boot | Doing | P0 | `05-Labs/QEMU-Boot-openEuler.md` | Collect verified boot command |
| Kernel Source Map | Source Reading | openEuler | Doing | P0 | `04-Source-Reading/Kernel-Source-Map.md` | Fill source repository paths |
| Candidate Issues | Issue | openEuler | Backlog | P1 | `06-Issues-PRs/Candidate-Issues.md` | Select 3 issues to analyze |
