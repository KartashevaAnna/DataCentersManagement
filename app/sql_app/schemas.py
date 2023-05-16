from typing import List, Optional

from pydantic import BaseModel, Field


class WeatherSchema(BaseModel):
    temp: float
    pressure: float
    humidity: float


class WindSchema(BaseModel):
    speed: float
    gust: float


class WeatherReportSchema(BaseModel):
    main: WeatherSchema
    wind: WindSchema
    name: str = Field(..., description="city name")
