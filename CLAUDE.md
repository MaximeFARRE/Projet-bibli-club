# CLAUDE.md

Read `AGENTS.md` before starting.

- **Role**: Professional Software Engineer assisting with the Club Entrepreneur Library Manager app (Pôle Léonard de Vinci).

## Mandatory workflow

- Run `git branch` first.
- Never work on `main`.
- Create or use a dedicated branch:
  - `feat/...`
  - `fix/...`
  - `docs/...`
  - `chore/...`
  - `test/...`
- Read files before editing them.
- Make the smallest possible change.
- Preserve the current architecture.
- Commit after each logical step.
- Review `git diff` before finishing.

## Architecture law

```text
UI → Services → Repository / DB
```

* Never put business logic in UI files.
* Never put SQL, API calls, or data transformations in UI files.
* Reuse existing services before creating a new one.
* Keep persistence separate from business logic.
* Do not duplicate logic.
* Do not create unnecessary files.

## Change policy

* Prefer minimal, targeted changes.
* Do not rewrite a whole file if a small edit is enough.
* Do not perform broad refactors unless explicitly requested.
* Do not modify unrelated files.
* If a task is ambiguous, state your assumptions before making changes.

## Commit format

Use Conventional Commits:

* `feat: ...`
* `fix: ...`
* `docs: ...`
* `chore: ...`
* `test: ...`

Examples:

* `feat: add import validation service`
* `fix: prevent duplicate transactions`
* `docs: update README architecture section`
* `chore: update .gitignore`

## Before finishing

* Run tests if they exist.
* Review changed files.
* Check `git diff`.
* Confirm that no unrelated code was modified.
* Update documentation if needed.
* Summarize what changed and why.
