from fastapi import APIRouter

from app.models.weather_models import WeatherInput, WeatherOutput
from app.utils.weather_utils import get_coords, get_weather_by_city

router = APIRouter(prefix="/weather")

@router.get("/{city}", response_model=WeatherOutput)
async def get_weather(city: str):
    coords: tuple[str, str] = get_coords(city)
    weather = get_weather_by_city(coords)
    return weather

# response_model=WeatherOutput