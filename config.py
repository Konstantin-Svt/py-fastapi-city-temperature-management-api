from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "Temperature Managment API"
    DATABASE_URL: str = "sqlite+aiosqlite:///db.sqlite3"
    WEATHER_API_URL: str = "http://api.weatherapi.com/v1"
    WEATHER_API_KEY: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
