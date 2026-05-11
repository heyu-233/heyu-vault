---
type: concept
module: openeuler
status: seed
created: 2026-05-11
updated: 2026-05-11
source: https://atomgit.com/openeuler/kernel
tags:
  - openeuler
  - roadmap
---

# openEuler Kernel Roadmap

## Learning Track

1. Understand openEuler release branches and kernel branch naming.
2. Learn how openEuler carries patches relative to upstream Linux.
3. Follow SIG-Kernel issue labels and contribution rules.
4. Build a local workflow for reading, building, testing, and documenting changes.

## Source Reading Track

- Start from high-level docs and branch README files.
- Build a source map for boot, scheduler, memory, drivers, and networking.
- For each module, record:
  - entry points
  - important structs
  - key files
  - common debugging commands

## Contribution Track

- First contributions should prioritize reproducibility and documentation.
- Then move to small bugfixes or test additions.
- Avoid deep scheduler/MM changes until the source reading map is mature.

## Open Questions

- Which openEuler kernel branch should be used for labs?
- Which QEMU machine target best matches current learning goals?
- Which SIG-Kernel issues are suitable for a first PR?
