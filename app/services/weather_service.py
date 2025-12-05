from app.database.database import SessionLocal
from sqlalchemy.exc import SQLAlchemyError
import httpx
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

        async with httpx.AsyncClient() as client:
            for city in CITIES:
                try:
                    response = await client.get(
                        "https://api.openweathermap.org/data/2.5/weather",
                        params={"q": city, "appid": settings.open_weather_api}
                    )
                    response.raise_for_status()
                except Exception as e:
                    print(f"Failed to fetch weather for {city}: {e}")
                    continue

                data = response.json()
                city_name = city.split(",")[0]

                weather_data = dict(
                    weather=data.get("weather", [{}])[0].get("main"),
                    temperature=data.get("main", {}).get("temp"),
                    feels_like=data.get("main", {}).get("feels_like"),
                    humidity=data.get("main", {}).get("humidity"),
                    pressure=data.get("main", {}).get("pressure"),
                    wind_speed=data.get("wind", {}).get("speed"),
                    visibility=data.get("visibility"),
                )

                try:
                    existing = db.query(Weather).filter(Weather.city == city_name).first()

                    if existing:
                        for key, value in weather_data.items():
                            setattr(existing, key, value)
                        print(f"Updated: {city_name}")
                    else:
                        new_entry = Weather(city=city_name, **weather_data)
                        db.add(new_entry)
                        print(f"Inserted: {city_name}")

                    db.commit()
                except SQLAlchemyError as e:
                    db.rollback()
                    print(f"DB Error for {city_name}: {e}")
        
    except TimeoutException:
        print("⚠ Weather API request timed out")
        return
    except Exception as e:
        print(f"Some error occurred while fetching and storing weather data: {e}")
        return
    finally:
        db.close()