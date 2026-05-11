---
type: concept
module: openeuler
status: seed
created: 2026-05-11
updated: 2026-05-11
source:
tags:
  - roadmap
  - kernel
---

# Kernel Learning Roadmap

## Goal

Build a practical openEuler/Linux kernel knowledge system that can support:

- source reading
- QEMU and kernel build experiments
- openEuler issue analysis
- future PRs, blog posts, and interview preparation

## Phase 1: Working Environment

- Install or prepare openEuler VM/QEMU environment.
- Learn Git/AtomGit contribution flow.
- Build a simple kernel or inspect an existing openEuler kernel tree.
- Record common commands in [[../07-CheatSheets/Kernel-Build-Commands|Kernel Build Commands]].

## Phase 2: Kernel Big Picture

- Boot path: firmware, bootloader, kernel entry, init process.
- Process and scheduler: task_struct, context switch, CFS basics.
- Memory: virtual memory, page table, buddy allocator, slab/slub.
- Device driver model: platform device/driver, probe, device tree.
- Filesystem and VFS: inode, dentry, file operations.
- Network stack: socket, TCP/IP path, procfs/sysfs observability.
- Debugging: printk, ftrace, perf, eBPF, crash logs, GDB/QEMU.

## Phase 3: openEuler Specifics

- Understand openEuler kernel branches and relationship with upstream Linux.
- Track SIG-Kernel contribution rules.
- Learn how issue triage, patch submission, and review work.
- Build a small contribution path from documentation, tests, or bug reproduction.

## Phase 4: Output Loop

- Every concept note should link to one source-reading note or lab.
- Every lab should produce a short retrospective.
- Every issue analysis should map to kernel modules and candidate files.
- Every useful learning chunk should be convertible into a blog or resume bullet.

## First 4-Week Plan

| Week | Focus | Deliverable |
| --- | --- | --- |
| 1 | openEuler kernel overview and QEMU boot | One working boot log and lab note |
| 2 | Boot path and device driver model | Boot path source map and driver note |
| 3 | Scheduler and process basics | Scheduler note with key structs/functions |
| 4 | Candidate issue analysis | 3 issue notes and one contribution plan |
