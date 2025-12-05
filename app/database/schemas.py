from pydantic import BaseModel

class WeatherData(BaseModel):
    city: str
    weather: str
    temperature: float
    feels_like: float
    humidity: int
    pressure: int
    wind_speed: float
    visibility: int