from typing import List

import httpx
import pandas as pd
import requests
from bs4 import BeautifulSoup

from app.sql_app.database import SessionLocal
from app.sql_app.models import WeatherReport
from app.sql_app.schemas import WeatherReportSchema
from tmp import RESPONSE


def get_largest_cities() -> List[str]:
    session = requests.Session()
    html = session.get("https://en.wikipedia.org/wiki/List_of_largest_cities").content
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find("table", {"class": "wikitable"})
    data = pd.read_html(str(table))
    df = data[0].head(51)
    df = df.dropna()
    return [city[0] for city in df["City[a]"].values]


async def get_weather_reports(cities: List[str]) -> List[WeatherReportSchema]:
    weather_report = []
    async with httpx.AsyncClient() as client:
        for city in cities:
            # url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={APIKEY}&units=metric"
            # response = await client.get(url)
            # response = response.json()
            tmp = WeatherReportSchema(**RESPONSE)
            weather_report.append(tmp)
        return weather_report


def save_to_db(weather: WeatherReportSchema):
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
