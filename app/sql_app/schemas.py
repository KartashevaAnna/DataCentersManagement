from typing import List, Optional

from pydantic import BaseModel


class WeatherReportPydantic(BaseModel):
    id: int
    name: str
    temperature: str

    class Config:
        orm_mode = True
