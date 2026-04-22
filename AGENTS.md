# Agent Operating Manual

Read this file before making any change in the repository.

**Context**: This is the library management system for the Club Entrepreneur student association (Pôle Léonard de Vinci).
The rules below must be followed strictly.

---

## Workflow

1. Read the existing code and documentation before editing anything.
2. Check the current branch with `git branch`.
3. Never work directly on `main`.
4. Create or use a dedicated branch:
   - `feat/...`
   - `fix/...`
   - `docs/...`
   - `chore/...`
   - `test/...`
5. Make small, focused changes.
6. Commit after each logical step.
7. Review the diff before finishing.

---

## Commit rules

- Never batch unrelated changes in one commit.
- Use Conventional Commits:
  - `feat: add portfolio import service`
  - `fix: correct date parsing in dashboard`
  - `docs: rewrite README and setup guide`
  - `chore: update .gitignore`
- Commit frequently. A large task should usually produce several commits.
- Never leave many modified files uncommitted.
- **MANDATORY**: Make at least 1 commit per file modified or created. You can and should make multiple commits on the same file if you add multiple functions.
- **MANDATORY**: Create a new commit for each notable function or feature created.
- **MANDATORY**: Never exceed 200 lines of code changed in a single commit. Stop and commit before continuing.

---

## Architecture rules

Always preserve a clear separation of concerns.

Preferred architecture:

```text
UI / pages / components
        ↓
services / business logic
        ↓
repositories / api / database layer
```

Rules:

* UI files only handle display and user interaction.
* Never put business logic, calculations, SQL, API calls, or data transformations inside UI files.
* All business logic belongs in dedicated services/ or domain modules.
* Database access belongs in repositories/, db/, api/, or equivalent.
* Never mix persistence and business logic in the same file.
* Reuse existing services before creating a new one.
* Do not duplicate logic.
* Create a new file only if no existing file is suitable.

---

## File and code rules
* Prefer minimal, targeted changes.
* Do not rewrite a whole file if a small edit is enough.
* Keep functions focused and easy to read.
* Prefer explicit names over short names.
* Avoid dead imports and unused variables.
* Never use except: pass.
* Add or update documentation when behavior changes.
* If tests exist, update or add tests for changed behavior.
* Never claim something was tested if it was not actually run.

---

## Documentation rules

The repository should always contain:

* README.md
* AGENTS.md
* CLAUDE.md
* CONTRIBUTING.md
* LICENSE
* docs/ARCHITECTURE.md if the project is non-trivial
* docs/DEVELOPMENT.md for setup and commands

README requirements:

* 3 to 6 GitHub badges
* Short project description
* Features
* Tech stack
* Installation
* Usage
* Repository structure
* Contributors
* Limitations

---

## Never do
* Never commit directly to main
* Never make broad refactors unless explicitly requested
* Never silently change architecture
* Never put business logic in UI files
* Never create unnecessary files
* Never rename or delete files without a good reason
* Never mix unrelated fixes in one task
* Never invent implementation details without reading the code first

---

## Definition of done

Before finishing a task:

- [ ] Correct branch used
- [ ] Small logical commits created
- [ ] Diff reviewed
- [ ] Documentation updated if needed
- [ ] No business logic added to UI
- [ ] No duplicated logic introduced
- [ ] Tests run if relevant
- [ ] No unrelated files modified
