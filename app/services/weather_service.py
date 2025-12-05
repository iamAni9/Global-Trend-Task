from app.database.database import SessionLocal
import httpx
# import asyncio
from app.settings import settings
from app.database.models import Weather
from httpx import TimeoutException

CITIES = [
    "Delhi,IN",
    "Mumbai,IN",
    "Kolkata,IN",
    "Chennai,IN",
    "Bengaluru,IN",
    "Hyderabad,IN",
    "Pune,IN",
    "Ahmedabad,IN",
    "Jaipur,IN",
    "Surat,IN",
]


async def get_and_save_indian_weather_data():
    try:
        db = SessionLocal()
        for city in CITIES:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    "https://api.openweathermap.org/data/2.5/weather",
                    params={"q": city, "appid": settings.open_weather_api}
                )
            data = response.json()
            weather_data = dict(
                city=city.split(',')[0],
                weather=data.get("weather", [{}])[0].get("main"),
                temperature=data.get("main", {}).get("temp"),
                feels_like=data.get("main", {}).get("feels_like"),
                humidity=data.get("main", {}).get("humidity"),
                pressure=data.get("main", {}).get("pressure"),
                wind_speed=data.get("wind", {}).get("speed"),
                visibility=data.get("visibility"),
            )   
            weather_entry = Weather(**weather_data)
            try:
                db.add(weather_entry)
                db.commit()
                db.refresh(weather_entry)
            except Exception as e:
                db.rollback()
                print("Error saving weather:", e)
                
        db.close()
        
    except TimeoutException:
        print("⚠ Weather API request timed out")
        return
    except Exception as e:
        print(f"Some error occurred while fetching and storing weather data: {e}")
        return

# asyncio.run(get_and_save_indian_weather_data())