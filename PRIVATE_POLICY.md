---
type: index
module: openeuler
status: seed
created: 2026-05-12
updated: 2026-05-12
source:
tags:
  - privacy
  - git
  - publishing
---

# Private Policy

This repository may be public or synced across devices. Treat every committed file as potentially public.

## Do Not Commit

- Resume originals with phone numbers, email screenshots, ID cards, or application forms.
- Verification codes, passwords, access tokens, SSH keys, API keys, cookies, or session data.
- Private chat logs, private application review material, or non-public school/company material.
- Large binaries such as VM images, ISO files, disk images, videos, or archives.
- Obsidian local workspace state such as `.obsidian/`.
- Private attachments under `Attachments/private/`.

## Allowed

- Markdown notes without sensitive personal data.
- Public links, public documentation, public issue/PR analysis.
- Small public images that are useful for technical notes.
- Commands, configs, and troubleshooting notes with secrets removed.

## Before Push Checklist

```powershell
git status --short
python .\tools\check_vault.py
```

If a file looks private, keep it outside the repository or place it under an ignored private path.
