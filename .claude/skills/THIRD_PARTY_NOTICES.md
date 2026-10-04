# Skills tiers embarqués

Ces skills sont copiés depuis le plugin `consulting-skills`
(https://github.com/yannick-bottino/consulting-claude-skills) pour que le plugin
Anchor Strategy B Corp tool fonctionne seul. Ils restent sous leur licence d'origine :

> MIT License — Copyright (c) Yannick Bottino
> Permission is hereby granted, free of charge, to any person obtaining a copy of this
> software and associated documentation files, to deal in the Software without restriction,
> subject to the inclusion of this copyright notice and permission notice in all copies or
> substantial portions of the Software. THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY
> OF ANY KIND.

| Skill | Copié le | Modifications |
|---|---|---|
| project-memory | 2026-10-04 | aucune |
| file-naming-standard | 2026-10-04 | aucune |
| humanize-output | 2026-10-04 | chemin de `last_updated.txt` passé en `${CLAUDE_PLUGIN_ROOT}/.claude/skills/...` |
| de-slop | 2026-10-04 | aucune |
| folder-analyzer-optimizer | 2026-10-04 | artefacts de développement retirés (CLAUDE.md, MEMORY.md, tasks/, docs/) |

Pour les mettre à jour : recopier depuis `consulting-skills`, puis relancer `python3 -m pytest`.
