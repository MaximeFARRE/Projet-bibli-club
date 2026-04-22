# Development Guide

## Environment Setup
1. Clone the repository and navigate to the project root.
2. Create a virtual environment: `python -m venv venv`
3. Activate the environment: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`

## Adding a New Page
Streamlit natively handles routing via the file system.
To add a new feature page:
1. Create a Python file in the `pages/` directory.
2. Prefix it with the next logical number (e.g., `07_Statistiques.py`).

## Database Configuration (Local vs Cloud)
By default, the application uses a local SQLite database (`data/bibliotheque.db`).

**To use Neon PostgreSQL:**
Create a `.streamlit/secrets.toml` file at the root of the project (this file is git-ignored) and add your connection string:
```toml
DATABASE_URL = "postgresql://user:password@ep-cool-pine-123456.eu-central-1.aws.neon.tech/dbname"
```
The `database.py` factory will automatically detect this and switch to the Postgres driver.

## Testing Notifications
Do not hardcode SMTP credentials. Add them to your `.streamlit/secrets.toml` to safely test the email features locally.
