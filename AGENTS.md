# Repository agent instructions

This repository formalizes Theorems A and B of `blueprint/triangles_in_the_plane_blueprint.tex` in Lean 4 +
Mathlib. Before working, read:

1. [automation/Instructions.md](automation/Instructions.md) — project rules and the current distilled user
   instructions (raw prompts in `automation/raw.md`).
2. [meta/Conventions.md](meta/Conventions.md) — Lean design conventions and the section → file map.
3. [automation/Status.md](automation/Status.md) — the status ledger (one entry per blueprint label).
4. [automation/ErrorReport.md](automation/ErrorReport.md) — blueprint errors and deviations.

Codex agents follow `.codex/skills/autoformalize/SKILL.md` when present, otherwise
`~/.codex/skills/autoformalize/SKILL.md` (or `$CODEX_HOME/skills/autoformalize/SKILL.md`). Claude agents use
[.claude/skills/autoformalize/SKILL.md](.claude/skills/autoformalize/SKILL.md).

The user's current explicit instructions take precedence over all repository guidance. Local automation
instructions supersede conflicting skill guidance.

All generated Lean code lives in the repository-root `Auto/` folder (one subfolder per blueprint section), in
the namespace `Auto`; `Auto.lean` imports every non-scratch file. Check files with
`lake env lean Auto/<Folder>/<File>.lean`, build with `lake build`. Update statuses with
`python3 meta/setstatus.py LABEL STATUS "Lean names"`, which also updates the blueprint metadata.
