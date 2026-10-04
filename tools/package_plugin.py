#!/usr/bin/env python3
"""Construit le zip du plugin à téléverser dans Cowork / claude.ai.

Usage : python3 tools/package_plugin.py [dossier_sortie]   (défaut : dist/)

Cowork n'accepte aucun dossier caché hormis .claude-plugin/ : on exclut .claude/, .git/, .gitignore,
ainsi que les dossiers de développement (tests/, tools/, docs/, dist/).
"""
from __future__ import annotations

import json
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEV_DIRS = {"tests", "tools", "docs", "dist"}


def included(rel: Path) -> bool:
    parts = rel.parts
    if parts[0] in DEV_DIRS or "__pycache__" in parts or rel.suffix == ".pyc":
        return False
    return all(not p.startswith(".") for p in parts) or parts[0] == ".claude-plugin"


def build(out_dir: Path = ROOT / "dist") -> Path:
    manifest = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / f"{manifest['name']}-{manifest['version']}.zip"
    with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as z:
        for path in sorted(ROOT.rglob("*")):
            rel = path.relative_to(ROOT)
            if path.is_file() and included(rel):
                z.write(path, rel.as_posix())
    return target


if __name__ == "__main__":
    print(build(Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "dist"))
