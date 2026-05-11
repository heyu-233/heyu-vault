---
type: cheatsheet
module: openeuler
status: seed
created: 2026-05-11
updated: 2026-05-11
source:
tags:
  - git
  - atomgit
---

# Git AtomGit

## Basic Flow

```bash
git clone <repo>
git checkout -b <topic-branch>
git status
git add <files>
git commit -s -m "component: short summary"
git push origin <topic-branch>
```

## Before PR

```bash
git status
git log --oneline -5
git diff --check
```

## Notes

- Confirm repository contribution rules before large changes.
- Keep one PR focused on one issue.
