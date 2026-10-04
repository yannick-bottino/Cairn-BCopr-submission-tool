# Règles du dépôt Anchor Strategy B Corp tool

- **Plugin autoporteur (règle stricte).** Tout skill appelé par un skill du plugin est copié dans `.claude/skills/<nom>/` (déclaré dans `.claude-plugin/plugin.json`, champ `skills`). Le test `tests/test_self_contained.py` échoue si un skill cité manque. Toute copie est tracée dans `.claude/skills/THIRD_PARTY_NOTICES.md`.
- Aucun code d'exigence hors de `resources/standards-v2.2/bcorp_v2.2_requirements.csv`, lui-même extrait du PDF de `resources/standards-v2.2/_source/`.
- Les fichiers `resources/standards-v2.2/<Impact Area>/*.md` sont générés (`python3 tools/build_standard_md.py`) : ne jamais les modifier à la main.
- Aucune donnée client dans ce dépôt (noms, montants, prénoms) : anonymiser en `[Client A]`, `[co-prestataire]`, `[prénom]`, `[montant]`.
- La taille et le secteur B Lab ne sont jamais calculés : ils viennent de la plateforme (export PDF ou déclaration manuelle).
- Rien n'est publié sur app.bcorporation.net sans validation explicite, lot par lot.
- TDD : `python3 -m pytest -q` doit rester vert avant tout commit.
