---
type: source-reading
module: boot
status: seed
created: 2026-05-11
updated: 2026-05-11
source:
tags:
  - boot
  - source-reading
---

# Boot Path

## Why It Matters

Boot path reading connects firmware, bootloader, kernel image, initramfs, device tree, and the first userspace process.

## Entry Points

- architecture-specific kernel entry
- common kernel init
- init process launch

## Questions

- How does QEMU pass boot arguments?
- Where is the command line parsed?
- Where does driver initialization begin?

## Related Labs

- [[../05-Labs/QEMU-Boot-openEuler|QEMU Boot openEuler]]
