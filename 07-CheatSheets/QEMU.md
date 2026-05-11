---
type: cheatsheet
module: boot
status: seed
created: 2026-05-11
updated: 2026-05-11
source:
tags:
  - qemu
  - commands
---

# QEMU

## Common Flags

```bash
-m 2048
-smp 2
-nographic
-serial mon:stdio
-append "console=ttyS0"
```

## Debug Stub

```bash
-s -S
```

Use with [[GDB]].
