---
type: source-reading
module: openeuler
status: seed
created: 2026-05-11
updated: 2026-05-11
source: https://atomgit.com/openeuler/kernel
tags:
  - source-reading
  - kernel
---

# Kernel Source Map

## Why It Matters

This page is the entry map for source reading. It should answer: where do I start when studying a kernel mechanism or analyzing an issue?

## Major Areas

| Area | Typical Paths | Notes |
| --- | --- | --- |
| Boot | `arch/*/kernel/`, `init/` | architecture entry and common init |
| Scheduler | `kernel/sched/` | scheduling classes, runqueue, context switch |
| Memory | `mm/` | page allocation, VM, page faults |
| Drivers | `drivers/`, `include/linux/` | driver model, bus, platform devices |
| Filesystem | `fs/` | VFS and filesystem implementations |
| Network | `net/` | socket layer and protocols |
| Documentation | `Documentation/` | official kernel docs |

## Local Repository Candidates

- `D:\renheyu\ospp_discover\repos`
- openEuler kernel should be cloned separately when needed.

## Related Notes

- [[Boot-Path]]
- [[Scheduler-Path]]
- [[Driver-Model-Path]]
