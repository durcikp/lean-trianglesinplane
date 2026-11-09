# Repository agent instructions

This repository formalizes Theorems A and B of `blueprint/blueprint.tex` in Lean 4 +
Mathlib. Before working, read:

1. [automation/Instructions.md](automation/Instructions.md) — project rules.
2. [automation/raw.md](automation/raw.md) — the user's prompts (they override the rules); it also contains the
   Lean design conventions and the section → file map (section "Content of `meta/Conventions.md`").
3. [automation/Status.md](automation/Status.md) — the status ledger (one entry per blueprint label).
4. [automation/ErrorReport.md](automation/ErrorReport.md) — blueprint errors and deviations.

Codex agents follow `.codex/skills/autoformalize/SKILL.md` when present, otherwise
`~/.codex/skills/autoformalize/SKILL.md` (or `$CODEX_HOME/skills/autoformalize/SKILL.md`). Claude agents use
[.claude/skills/autoformalize/SKILL.md](.claude/skills/autoformalize/SKILL.md).

The user's current explicit instructions take precedence over all repository guidance. Local automation
instructions supersede conflicting skill guidance.

All generated Lean code lives in the `TrianglesInThePlane/Auto/` folder (one subfolder per blueprint
section), in the namespace `Auto`; the root module `TrianglesInThePlane.lean` imports every non-scratch
file. Check files with `lake env lean TrianglesInThePlane/Auto/<Folder>/<File>.lean`, build with
`lake build`. When a status in `automation/Status.md` changes, update the matching `\lean{}`/`\leanok` metadata in `blueprint/blueprint.tex` as well.
