"""Règle stricte du dépôt : le plugin est autoporteur, dans Claude Code comme dans Cowork."""
import json
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
NAME_RE = re.compile(r"`([a-z0-9]+(?:-[a-z0-9]+)+)`")
KNOWN = {"humanize-output", "de-slop", "project-memory", "file-naming-standard", "folder-analyzer-optimizer",
         "b-corp-platform-navigation", "b-corp-gap-analysis-excel", "entretien-cadrage-bcorp", "proposal-rse",
         "cowork-plugin", "project-init"}
OWN = {"bcorp-gap-analysis", "bcorp-evidence-pack", "bcorp-platform-plan"}

sys.path.insert(0, str(ROOT / "tools"))
import package_plugin  # noqa: E402


def skill_names():
    return {p.parent.name for p in SKILLS.glob("*/SKILL.md")}


def test_skills_live_in_default_folder_only():
    manifest = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
    assert "skills" not in manifest            # dossier par défaut skills/ : chargé par Claude Code et Cowork
    assert not (ROOT / ".claude" / "skills").exists()


def test_every_called_skill_is_embedded():
    available = skill_names()
    missing = {}
    for name in OWN:
        text = (SKILLS / name / "SKILL.md").read_text(encoding="utf-8")
        called = {n for n in NAME_RE.findall(text) if n in KNOWN}
        if called - available:
            missing[name] = sorted(called - available)
    assert not missing, f"skills appelés mais non embarqués dans skills/ : {missing}"


def test_embedded_skills_are_traced():
    notices = (ROOT / "THIRD_PARTY_NOTICES.md").read_text(encoding="utf-8")
    for name in skill_names() - OWN:
        assert f"| {name} |" in notices, name


def test_plugin_root_paths_exist():
    for skill in SKILLS.glob("*/SKILL.md"):
        for rel in re.findall(r"\$\{CLAUDE_PLUGIN_ROOT\}/([^\s`\"')]+)", skill.read_text(encoding="utf-8")):
            if "<" in rel:
                rel = rel.split("<")[0]
            assert (ROOT / rel).exists(), f"{skill.parent.name} : {rel}"


def test_no_hardcoded_mnt_paths():
    offenders = [str(p.relative_to(ROOT)) for p in SKILLS.rglob("*.md")
                 if "/mnt/skills/" in p.read_text(encoding="utf-8")]
    assert not offenders, offenders


def test_cowork_package(tmp_path):
    z = package_plugin.build(tmp_path)
    names = zipfile.ZipFile(z).namelist()
    assert ".claude-plugin/plugin.json" in names
    assert "skills/de-slop/SKILL.md" in names and "skills/bcorp-gap-analysis/SKILL.md" in names
    assert any(n.startswith("resources/standards-v2.2/1-PSG") for n in names)
    assert "shared/lib/bcorp_ref.py" in names
    hidden = [n for n in names if any(part.startswith(".") for part in n.split("/")) and not n.startswith(".claude-plugin/")]
    assert not hidden, hidden[:5]
    assert not any(n.startswith(("tests/", "tools/", "docs/")) or "__pycache__" in n for n in names)
