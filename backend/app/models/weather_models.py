from pydantic import BaseModel, Field


class WeatherInput(BaseModel):
    city: str  # Field(examples=['London', 'Paris', 'Moscow'], min_length=1, max_length=30)


class WeatherOutput(BaseModel):
    time: list[str]
    temperature_2m: list[float]
