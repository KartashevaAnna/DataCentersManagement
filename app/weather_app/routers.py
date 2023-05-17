import os

from dotenv import load_dotenv
from fastapi import APIRouter

from app.tools.helpers import get_largest_cities, get_weather_reports, save_to_db

load_dotenv()

APIKEY = os.getenv("OPENWEATHERAPIKEY")

router = APIRouter()


@router.post("/get-weather-report")
async def get_weather_report():
    cities = get_largest_cities()
    weather_reports = await get_weather_reports(cities)
    for weather in weather_reports:
        save_to_db(weather)
    return "OK"
