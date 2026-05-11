---
type: cheatsheet
module: debugging
status: seed
created: 2026-05-11
updated: 2026-05-11
source:
tags:
  - gdb
  - commands
---

# GDB

## Attach To QEMU

```bash
gdb vmlinux
(gdb) target remote :1234
(gdb) b start_kernel
(gdb) c
```

## Useful Commands

```gdb
bt
info registers
list
disassemble
```
