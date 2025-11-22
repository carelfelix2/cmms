# CMMS Backend (FastAPI)

This repository contains a modular FastAPI skeleton for a CMMS (Computerized Maintenance Management System).

Structure:
- `app/` - main package
  - `config/` - settings
  - `database/` - SQLAlchemy connection
  - `models/`, `schemas/`, `repositories/`, `services/`, `routers/` per domain

Quick start (Windows PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Environment variables:
- `DATABASE_URL` (overrides `config.settings.settings.database_url`)
- `SECRET_KEY` (overrides `config.settings.settings.secret_key`)

Notes:
- This is a starter skeleton. Implement business logic, validations, and migrations (Alembic) as needed.
