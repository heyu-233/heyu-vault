---
type: source-reading
module: driver
status: seed
created: 2026-05-11
updated: 2026-05-11
source:
tags:
  - driver
  - source-reading
---

# Driver Model Path

## Why It Matters

Driver model reading connects device tree, bus matching, probe, resources, interrupts, and user-visible device nodes.

## Entry Points

- platform bus registration
- driver probe callback
- device tree matching
- character device or misc device registration

## Questions

- How is a device matched with a driver?
- Where are resources parsed from device tree?
- How does an interrupt handler get registered?
