**Global Trend**

A small FastAPI service for collecting and exposing weather-related trend data. The project provides a web API, background scheduler jobs to fetch/update data, and a simple SQLAlchemy-based persistence layer.

**Quick Start**
- **Python:** Use Python 3.11 or later.
- **Virtualenv:** Create and activate a virtual environment (Windows PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

- **Dependencies:** Install project dependencies. If you have a `requirements.txt`, use:

```powershell
pip install -r requirements.txt
```

Otherwise install the typical runtime packages:

```powershell
pip install fastapi uvicorn[standard] sqlalchemy psycopg2-binary httpx apscheduler python-dotenv
```

**Run the application**
- **Option A (recommended):** Start with Uvicorn:

```powershell
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

- **Option B:** Run the provided entry point if present:

```powershell
python run.py
```

- **Open API docs:** Visit `http://localhost:8000/docs` to explore endpoints and schemas.

**Project Layout**
- **`run.py`**: Optional app entry script.
- **`app/main.py`**: FastAPI application factory and startup events.
- **`app/settings.py`**: Configuration and environment variable loading.
- **`app/database/`**: Database initialization and models (`database.py`, `models.py`, `schemas.py`).
- **`app/routers/`**: API route definitions (e.g. `weather_data_route.py`).
- **`app/services/`**: Business logic and HTTP integrations (e.g. `weather_service.py`).
- **`app/scheduler/`**: Background jobs and scheduling logic (e.g. `job.py`).

**Configuration & Environment**
- **`.env`**: Put environment variables here (not committed). Typical keys:
  - `DATABASE_URL` — SQLAlchemy/DB connection string (e.g. PostgreSQL)
  - `WEATHER_API_KEY` — third-party weather API key (if used)
  - `SCHEDULER_ENABLED` — enable/disable scheduled jobs (true/false)

- The app loads configuration in `app/settings.py`; check that file to see all supported variables.

**Database**
- The project uses SQLAlchemy in `app/database/database.py`. Update `DATABASE_URL` to point to your database.
- If you use PostgreSQL locally, create the DB and run any initialization scripts from `app/database` (the project does not include Alembic migrations by default).

**Scheduler / Background Jobs**
- Scheduled tasks are defined in `app/scheduler/job.py` and are powered by APScheduler. These tasks usually call functions in `app/services/` to fetch or process remote weather data.

**API Notes**
- The weather-related endpoints are declared in `app/routers/weather_data_route.py`. Example endpoints and request/response models are visible in the interactive docs at `http://localhost:8000/docs`.
- For programmatic checks you can curl the server or call endpoints with `httpx`.

**Development**
- Use the `--reload` flag with Uvicorn for fast iteration.
- Activate your virtual environment before running commands: `.\.venv\Scripts\Activate.ps1` (PowerShell) or `.\.venv\Scripts\activate` (cmd).

**Tests & Linting**
- There are no test files included by default. You can add tests under a `tests/` folder and run them with `pytest`.

**Deployment**
- For production deploy, run Uvicorn with multiple workers behind a reverse proxy. Use a production database and set `SCHEDULER_ENABLED=false` if you prefer running scheduled jobs separately (e.g., in a dedicated worker process).

**Troubleshooting**
- If the app can't connect to the DB, confirm `DATABASE_URL` and network access.
- If scheduled jobs don't start, check `SCHEDULER_ENABLED` and the startup logic in `app/main.py`.

**Contributing**
- Open issues or pull requests with clear descriptions and reproducible steps. Keep changes focused and include tests where appropriate.

**License**
- This repository does not include a license file. Add `LICENSE` if you want to make the project open source.

---
If you want, I can also:
- generate a `requirements.txt` from the current environment,
- add a sample `.env.example`, or
- add simple health-check and README badges.
