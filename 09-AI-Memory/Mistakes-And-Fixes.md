---
type: output
module: openeuler
status: seed
created: 2026-05-12
updated: 2026-05-12
source:
tags:
  - ai-memory
  - mistakes
  - fixes
---

# Mistakes And Fixes

Use this note to record mistakes that should not be repeated.

## Format

```markdown
## YYYY-MM-DD - Short Title

- Context:
- Mistake:
- Root cause:
- Fix:
- Prevention:
- Related files:
```

## 2026-05-12 - GitHub Actions Index Order Failure

- Context: `tools/sync_kb_index.py --check` passed on Windows but failed on GitHub Actions Ubuntu.
- Mistake: The index freshness check compared generated Markdown exactly while file ordering was platform-dependent.
- Root cause: path sorting differed between Windows-like local behavior and Linux case-sensitive ordering.
- Fix: Sort index paths by lowercase relative path plus original relative path.
- Prevention: Keep index generation deterministic across platforms and print the first differing line when a stale index is detected.
- Related files: `tools/sync_kb_index.py`, `indexes/kb-index.md`, `indexes/llm-index.md`.
