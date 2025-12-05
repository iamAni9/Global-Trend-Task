from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.routers import weather_data_route
from fastapi.middleware.cors import CORSMiddleware
from app.database.database import Base, engine
from app.services.weather_service import get_and_save_indian_weather_data
from app.scheduler.job import start_scheduler

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Creating tables...")
    Base.metadata.create_all(bind=engine)

    print("Fetching initial weather...")
    await get_and_save_indian_weather_data()

    print("Starting scheduler...")
    scheduler = start_scheduler(app)

    yield

    print("Shutting down scheduler...")
    scheduler.shutdown()

app = FastAPI(
    title="Global Trend API",
    description="Backend API for Global Trend Application",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(weather_data_route.route)

@app.get("/")
async def read_root():
    return {"App is working": True}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}