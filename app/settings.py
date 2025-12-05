from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    open_weather_api: str
    supabase_url: str

    class Config:
        env_file = ".env"

settings = Settings()