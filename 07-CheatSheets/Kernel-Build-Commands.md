---
type: cheatsheet
module: openeuler
status: seed
created: 2026-05-11
updated: 2026-05-11
source:
tags:
  - kernel
  - build
  - commands
---

# Kernel Build Commands

## Inspect Source

```bash
git status
git branch -a
git log --oneline -5
```

## Configure

```bash
make defconfig
make menuconfig
```

## Build

```bash
make -j$(nproc)
make modules -j$(nproc)
```

## Clean

```bash
make clean
make mrproper
```

## Notes

- Record exact branch, config, compiler, and architecture.
- Do not treat a command as verified until it has been run in the target environment.
