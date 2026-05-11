---
type: lab
module: debugging
status: seed
created: 2026-05-11
updated: 2026-05-11
source:
tags:
  - gdb
  - qemu
  - debugging
---

# Debug Kernel With GDB

## Goal

Use QEMU + GDB to stop at kernel entry or a selected breakpoint.

## Steps

1. Build kernel with debug symbols.
2. Boot QEMU with GDB stub.
3. Attach GDB.
4. Set breakpoints.
5. Record call stack and source location.

## Related Cheat Sheet

- [[../07-CheatSheets/GDB|GDB]]
