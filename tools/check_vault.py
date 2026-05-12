#!/usr/bin/env python3
"""Basic quality checks for heyu-vault."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_KEYS = {"type", "module", "status", "created", "updated", "tags"}
FRONTMATTER_EXEMPT = {
    "README.md",
}
EXEMPT_PREFIXES = {
    ".github/",
}
SKIP_DIRS = {".git", ".obsidian"}
SENSITIVE_PATTERNS = [
    "resume",
    "cv",
    "token",
    "secret",
    "password",
    "id_rsa",
    "id_ed25519",
    "身份证",
    "申请表原件",
    "简历",
    "phone",
    "cookie",
]
SENSITIVE_PATH_ALLOWLIST = {
    "08-Outputs/Resume-Materials.md",
}
MAX_ATTACHMENT_BYTES = 10 * 1024 * 1024
WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")


def parse_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---", 4)
    if end == -1:
        return {}, text
    block = text[4:end].splitlines()
    body = text[text.find("\n", end + 1) + 1 :]
    data: dict[str, Any] = {}
    current_key: str | None = None
    for raw in block:
        line = raw.rstrip()
        if not line.strip():
            continue
        if line.startswith("  - ") and current_key:
            data.setdefault(current_key, [])
            if not isinstance(data[current_key], list):
                data[current_key] = []
            data[current_key].append(line[4:].strip())
            continue
        if ":" in line:
            key, value = line.split(":", 1)
            current_key = key.strip()
            data[current_key] = value.strip()
    return data, body


def iter_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        rel_parts = path.relative_to(ROOT).parts
        if any(part in SKIP_DIRS for part in rel_parts):
            continue
        files.append(path)
    return sorted(files)


def iter_markdown() -> list[Path]:
    return [p for p in iter_files() if p.suffix.lower() == ".md"]


def has_h1(body: str) -> bool:
    return any(line.startswith("# ") for line in body.splitlines())


def is_frontmatter_exempt(rel: str) -> bool:
    if rel in FRONTMATTER_EXEMPT:
        return True
    return any(rel.startswith(prefix) for prefix in EXEMPT_PREFIXES)


def note_candidates(target: str, current: Path) -> list[Path]:
    raw = target.strip()
    if raw.startswith(("http://", "https://", "mailto:")):
        return []
    names = [raw, f"{raw}.md"]
    candidates = []
    for name in names:
        p = (current.parent / name).resolve()
        candidates.append(p)
        p2 = (ROOT / name).resolve()
        candidates.append(p2)
    stem = Path(raw).stem
    candidates.extend(p.resolve() for p in ROOT.rglob(f"{stem}.md"))
    return candidates


def link_exists(target: str, current: Path) -> bool:
    candidates = note_candidates(target, current)
    if not candidates:
        return True
    root_resolved = ROOT.resolve()
    for candidate in candidates:
        try:
            candidate.relative_to(root_resolved)
        except ValueError:
            continue
        if candidate.exists():
            return True
    return False


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    for path in iter_markdown():
        rel = path.relative_to(ROOT).as_posix()
        text = path.read_text(encoding="utf-8")
        meta, body = parse_frontmatter(text)

        if not has_h1(body if meta else text):
            errors.append(f"{rel}: missing H1 heading")

        if not is_frontmatter_exempt(rel):
            if not meta:
                errors.append(f"{rel}: missing frontmatter")
            else:
                missing = sorted(k for k in REQUIRED_KEYS if k not in meta)
                if missing:
                    errors.append(f"{rel}: missing frontmatter keys: {', '.join(missing)}")

        for match in WIKILINK_RE.finditer(text):
            target = match.group(1)
            if not link_exists(target, path):
                errors.append(f"{rel}: broken wikilink [[{target}]]")

    for path in iter_files():
        rel = path.relative_to(ROOT).as_posix()
        lowered = rel.lower()
        if rel not in SENSITIVE_PATH_ALLOWLIST and any(
            pattern.lower() in lowered for pattern in SENSITIVE_PATTERNS
        ):
            errors.append(f"{rel}: path looks sensitive")
        if rel.startswith("Attachments/") and path.stat().st_size > MAX_ATTACHMENT_BYTES:
            warnings.append(f"{rel}: attachment larger than 10MB")

    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")

    if errors:
        print(f"Vault check failed: {len(errors)} error(s), {len(warnings)} warning(s)")
        return 1
    print(f"Vault check passed: {len(iter_markdown())} markdown files, {len(warnings)} warning(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
