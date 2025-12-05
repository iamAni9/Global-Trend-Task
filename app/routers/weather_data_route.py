from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.database.models import Weather

route = APIRouter(
    prefix="/weather",
    tags=["weather"],
)

@route.get("/")
async def get_weather_data(db: Session = Depends(get_db)):
    try:
        weather_data = db.query(Weather).all()
        return weather_data
    except Exception as e:
        return {"error": str(e)}

@route.get("/{city}")
async def get_weather_by_city(city: str, db: Session = Depends(get_db)):
    try:
        weather_entry = db.query(Weather).filter(Weather.city == city).first()
        if weather_entry:
            return weather_entry
        else:
            return {"error": "City not found"}
    except Exception as e:
        return {"error": str(e)}