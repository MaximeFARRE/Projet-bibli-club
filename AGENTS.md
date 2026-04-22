# Agent Operating Manual

Read this before making changes to the repository.

## Repository Structure
- **UI Layer**: `Accueil.py` and `pages/*.py`. These files handle presentation only.
- **Data Layer**: `database.py`. The single source of truth for all SQL queries and connections.
- **Service Layer**: `email_utils.py`, `notifications.py`. Contains business logic.

## Commands
- **Run**: `streamlit run Accueil.py`
- **Install**: `pip install -r requirements.txt`

## Git Workflow & Style
1. Never commit directly to `main`.
2. Create dedicated branches (`feat/...`, `fix/...`, `docs/...`).
3. Commit frequently using Conventional Commits (`feat: ...`, `fix: ...`).

## Architectural Rules
1. **No UI Business Logic**: Never put raw SQL queries, heavy calculations, or email logic inside `pages/*.py`.
2. **Persistence Separation**: All data read/write operations must happen inside `database.py`.
3. **Minimal Changes**: Do not perform broad refactors. Modify only what is strictly necessary to fulfill the request.
