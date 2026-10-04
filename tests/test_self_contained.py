"""Règle stricte du dépôt : tout skill appelé par un skill du plugin est embarqué."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EMBEDDED = ROOT / ".claude" / "skills"
OWN = ROOT / "skills"
NAME_RE = re.compile(r"`([a-z0-9]+(?:-[a-z0-9]+)+)`")


def skill_names(folder):
    return {p.parent.name for p in folder.glob("*/SKILL.md")}


def test_plugin_declares_embedded_skills():
    manifest = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
    assert manifest["skills"] == ["./skills", "./.claude/skills"]


def test_every_called_skill_is_embedded():
    available = skill_names(EMBEDDED) | skill_names(OWN)
    known_external = {"humanize-output", "de-slop", "project-memory", "file-naming-standard",
                      "folder-analyzer-optimizer", "b-corp-platform-navigation", "b-corp-gap-analysis-excel",
                      "entretien-cadrage-bcorp", "proposal-rse", "cowork-plugin"}
    missing = {}
    for skill in OWN.glob("*/SKILL.md"):
        called = {n for n in NAME_RE.findall(skill.read_text(encoding="utf-8")) if n in known_external}
        if called - available:
            missing[skill.parent.name] = sorted(called - available)
    assert not missing, f"skills appelés mais non embarqués dans .claude/skills/ : {missing}"


def test_embedded_skills_are_traced():
    notices = (EMBEDDED / "THIRD_PARTY_NOTICES.md").read_text(encoding="utf-8")
    for name in skill_names(EMBEDDED):
        assert f"| {name} |" in notices, name


def test_no_hardcoded_mnt_paths():
    offenders = [str(p.relative_to(ROOT)) for p in EMBEDDED.rglob("*.md")
                 if "/mnt/skills/" in p.read_text(encoding="utf-8")]
    assert not offenders, offenders
