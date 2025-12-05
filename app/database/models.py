from app.database.database import Base
from sqlalchemy import Column, Integer, String, Float

class Weather(Base):
    __tablename__ = "weather_data"
    
    id = Column(Integer, primary_key=True)
    city = Column(String, unique=True, index=True)
    weather = Column(String)
    temperature = Column(Integer)
    feels_like = Column(Integer)
    humidity = Column(Integer)
    pressure = Column(Integer)
    wind_speed = Column(Float)
    visibility = Column(Integer)