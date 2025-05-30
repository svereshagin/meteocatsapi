import pathlib
from pydantic_settings import SettingsConfigDict
from pydantic_settings import BaseSettings as PydanticBaseSettings
from pydantic import SecretStr

PREFIX = "METEOCATSAPI_"

DOTENV = pathlib.Path(__file__).parent.parent.parent / ".env"


class BaseSettings(PydanticBaseSettings):
    """Base settings."""

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )

class WeatherSettings(BaseSettings):
    base_forecast_url: str 
    api: str
    model_config = SettingsConfigDict(
        env_file=DOTENV, env_prefix=f"{PREFIX}WEATHER_", extra="ignore"
    )

class Settings(BaseSettings):
    """Main settings."""

    env: str = "local"
    host: str = "localhost"
    port: int = 8000
    workers: int = 1
    log_level: str = "info"
    reload: bool = False
    weather: WeatherSettings = WeatherSettings()
    model_config = SettingsConfigDict(
        env_file=DOTENV,
        env_prefix=PREFIX,
    )
    
settings = Settings()
