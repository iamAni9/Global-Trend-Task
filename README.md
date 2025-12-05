**Global Trend**

A small FastAPI service for collecting and exposing weather-related trend data. The project provides a web API, background scheduler jobs to fetch/update data, and a simple SQLAlchemy-based persistence layer.

#Tryout the API here 👉 https://globaltrendapitask.onrender.com/docs

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
- **Option A:** Start with Uvicorn:

```powershell
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

- **Option B (recommended):** Run the provided entry point if present:

```powershell
python run.py
```

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

- The app loads configuration in `app/settings.py`; check that file to see all supported variables.

**Database**
- Update `DATABASE_URL` to point to your postgres database.

**Scheduler / Background Jobs**
- Scheduled tasks are defined in `app/scheduler/job.py` and are powered by APScheduler. These tasks usually call functions in `app/services/` to fetch or process remote weather data every 30 minutes.
