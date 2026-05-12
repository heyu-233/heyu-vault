#!/usr/bin/env python3
"""Build a lightweight index for this Markdown/Obsidian vault."""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_VAULT = REPO_ROOT
DEFAULT_JSON = REPO_ROOT / "indexes" / "kb-index.json"
DEFAULT_MD = REPO_ROOT / "indexes" / "kb-index.md"
DEFAULT_LLM_JSON = REPO_ROOT / "indexes" / "llm-index.json"
DEFAULT_LLM_MD = REPO_ROOT / "indexes" / "llm-index.md"

WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")
MDLINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
TAG_RE = re.compile(r"(?<!\w)#([A-Za-z0-9_\-/]+)")
SKIP_DIRS = {".git", ".obsidian", "indexes"}
LLM_INCLUDE_DIRS = {
    "MOCs",
    "02-Kernel-Concepts",
    "04-Source-Reading",
    "05-Labs",
    "06-Issues-PRs",
    "07-CheatSheets",
}


def parse_scalar(value: str) -> Any:
    value = value.strip()
    if value == "":
        return ""
    if value.lower() in {"true", "false"}:
        return value.lower() == "true"
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        if not inner:
            return []
        return [x.strip().strip("\"'") for x in inner.split(",")]
    return value.strip("\"'")


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
            if not isinstance(data.get(current_key), list):
                data[current_key] = []
            data[current_key].append(line[4:].strip())
            continue
        if ":" in line:
            key, value = line.split(":", 1)
            current_key = key.strip()
            data[current_key] = parse_scalar(value)
    return data, body


def first_heading(body: str, fallback: str) -> str:
    for line in body.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return fallback


def normalize_tags(frontmatter_tags: Any, body: str) -> list[str]:
    tags: set[str] = set()
    if isinstance(frontmatter_tags, str) and frontmatter_tags:
        tags.add(frontmatter_tags)
    elif isinstance(frontmatter_tags, list):
        tags.update(str(x).strip() for x in frontmatter_tags if str(x).strip())
    tags.update(m.group(1) for m in TAG_RE.finditer(body))
    return sorted(tags)


def extract_links(body: str) -> list[str]:
    links = set()
    links.update(m.group(1).strip() for m in WIKILINK_RE.finditer(body))
    links.update(m.group(1).strip() for m in MDLINK_RE.finditer(body))
    return sorted(links)


def file_updated_at(path: Path) -> str:
    dt = datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc)
    return dt.isoformat(timespec="seconds")


def should_index(path: Path, vault: Path, profile: str) -> bool:
    rel_parts = path.relative_to(vault).parts
    if any(part in SKIP_DIRS for part in rel_parts):
        return False
    if profile == "llm":
        return bool(rel_parts) and rel_parts[0] in LLM_INCLUDE_DIRS
    return True


def index_file(path: Path, vault: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    meta, body = parse_frontmatter(text)
    rel = path.relative_to(vault).as_posix()
    title = str(meta.get("title") or first_heading(body, path.stem))
    return {
        "title": title,
        "path": rel,
        "type": meta.get("type", ""),
        "module": meta.get("module", ""),
        "status": meta.get("status", ""),
        "tags": normalize_tags(meta.get("tags", []), body),
        "links": extract_links(body),
        "updated_at": meta.get("updated") or file_updated_at(path),
    }


def build_index(vault: Path, profile: str) -> list[dict[str, Any]]:
    files = sorted(
        p for p in vault.rglob("*.md") if p.is_file() and should_index(p, vault, profile)
    )
    return [index_file(path, vault) for path in files]


def markdown_text(index: list[dict[str, Any]], profile: str) -> str:
    title = "heyu-vault LLM Index" if profile == "llm" else "heyu-vault Index"
    lines = [
        "---",
        "type: index",
        "module: openeuler",
        "status: seed",
        "created: 2026-05-12",
        "updated: 2026-05-12",
        "source:",
        "tags:",
        "  - index",
        "  - automation",
        "---",
        "",
        f"# {title}",
        "",
        "| Title | Type | Module | Status | Path | Tags |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for item in index:
        tags = ", ".join(item["tags"])
        lines.append(
            f"| {item['title']} | {item['type']} | {item['module']} | "
            f"{item['status']} | `{item['path']}` | {tags} |"
        )
    return "\n".join(lines) + "\n"


def default_output_paths(profile: str) -> tuple[Path, Path]:
    if profile == "llm":
        return DEFAULT_LLM_JSON, DEFAULT_LLM_MD
    return DEFAULT_JSON, DEFAULT_MD


def check_markdown_fresh(path: Path, expected: str, profile: str) -> bool:
    if not path.exists():
        print(f"ERROR: index file does not exist: {path}")
        return False
    actual = path.read_text(encoding="utf-8")
    if actual == expected:
        return True
    print(f"ERROR: index is stale: {path}")
    command = "python .\\tools\\sync_kb_index.py"
    if profile != "all":
        command = f"{command} --profile {profile}"
    print(f"Run: {command}")
    return False


def main() -> int:
    parser = argparse.ArgumentParser(description="Index vault Markdown notes.")
    parser.add_argument("--vault", type=Path, default=DEFAULT_VAULT)
    parser.add_argument("--out-json", type=Path)
    parser.add_argument("--out-md", type=Path)
    parser.add_argument("--profile", choices=("all", "llm"), default="all")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Verify the generated Markdown index matches the checked-in index.",
    )
    args = parser.parse_args()

    vault = args.vault.resolve()
    if not vault.exists():
        raise SystemExit(f"vault does not exist: {vault}")

    default_json, default_md = default_output_paths(args.profile)
    out_json = args.out_json or default_json
    out_md = args.out_md or default_md

    index = build_index(vault, args.profile)
    md = markdown_text(index, args.profile)
    js = json.dumps(index, ensure_ascii=False, indent=2)

    if args.check:
        print(f"Indexed {len(index)} notes")
        return 0 if check_markdown_fresh(out_md, md, args.profile) else 1

    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(js, encoding="utf-8")
    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_md.write_text(md, encoding="utf-8")

    print(f"Indexed {len(index)} notes")
    print(f"JSON: {out_json}")
    print(f"Markdown: {out_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
