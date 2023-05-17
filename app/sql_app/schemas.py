from typing import Optional

from pydantic import BaseModel, Field


class WeatherSchema(BaseModel):
    temp: float
    pressure: float
    humidity: float


class WindSchema(BaseModel):
    speed: float
    gust: Optional[float] = None


class WeatherReportSchema(BaseModel):
    main: WeatherSchema
    wind: WindSchema
    name: str = Field(..., description="city name")
