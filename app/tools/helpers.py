import os
from typing import List

import httpx
import pandas as pd
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi_utils.tasks import repeat_every

from app.sql_app.database import SessionLocal
from app.sql_app.models import WeatherReport
from app.sql_app.schemas import WeatherReportSchema

load_dotenv()
APIKEY = os.getenv("OPENWEATHERAPIKEY")


def get_largest_cities() -> List[str]:
    """Get the list of 50 largest world cities."""

    session = requests.Session()
    html = session.get("https://en.wikipedia.org/wiki/List_of_largest_cities").content
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find("table", {"class": "wikitable"})
    data = pd.read_html(str(table))
    df = data[0].head(51)
    df = df.dropna()
    return [city[0] for city in df["City[a]"].values]


async def get_weather_reports(cities: List[str]) -> List[WeatherReportSchema]:
    """Get a weather report for each city."""

    weather_report = []
    async with httpx.AsyncClient() as client:
        for city in cities:
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={APIKEY}&units=metric"
            response = await client.get(url)
            response = response.json()
            city_weather = WeatherReportSchema(**response)
            weather_report.append(city_weather)
        return weather_report


def save_to_db(weather: WeatherReportSchema):
    """Save report to database."""

    db = SessionLocal()
    db.add(
        WeatherReport(
            city=weather.name,
            temperature=weather.main.temp,
            pressure=weather.main.pressure,
            humidity=weather.main.humidity,
            wind_speed=weather.wind.speed,
            wind_gust=weather.wind.gust,
        )
    )
    db.commit()
    db.close()


def run_loop(app: FastAPI):
    """Run main loop: make a list of cities, request weather for them, save results to the database."""

    @app.on_event("startup")
    @repeat_every(seconds=60 * 60)
    async def get_weather_report():
        cities = get_largest_cities()
        weather_reports = await get_weather_reports(cities)
        for weather in weather_reports:
            save_to_db(weather)
