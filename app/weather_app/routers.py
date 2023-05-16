import os
import httpx
from fastapi import APIRouter
from dotenv import load_dotenv

from app.sql_app.database import SessionLocal
from app.sql_app.models import WeatherReport

load_dotenv()

APIKEY = os.getenv("OPENWEATHERAPIKEY")
CITIES = ["Shanghai", "Moscow"]

router = APIRouter()


@router.get("/cities/")
async def get_cities():
        return {"message": CITIES}

@router.get("/new_weather/")
async def request_weather():
    async with httpx.AsyncClient() as client:
        for city in CITIES:
            # url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={APIKEY}&units=metric"
            # response = await client.get(url)
            # response = response.json()
            response = {
                'coord': {'lon': 37.6156, 'lat': 55.7522},
                'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}],
                'base': 'stations',
                'main': {'temp': 20.27, 'feels_like': 19.34, 'temp_min': 19.49, 'temp_max': 20.81, 'pressure': 1022, 'humidity': 38,
     'sea_level': 1022, 'grnd_level': 1004},
                'visibility': 10000,
                'wind': {'speed': 4.89, 'deg': 155, 'gust': 5.51},
                'clouds': {'all': 5},
                'dt': 1684243786,
                'sys': {'type': 2, 'id': 47754, 'country': 'RU', 'sunrise': 1684199827, 'sunset': 1684258492}, 'timezone': 10800,
     'id': 524901, 'name': 'Moscow', 'cod': 200}
            temp = response["main"]["temp"]
            name = response["name"]
            db = SessionLocal()
            db.add(WeatherReport(city=name, temperature=temp))
            db.commit()
            db.close()
        db = SessionLocal()
        result = db.query(WeatherReport).all()
        db.close()
        return {"message": result}




@router.get("/")
async def show_weather():
    db = SessionLocal()
    result = db.query(WeatherReport).all()
    db.close()
    return {"message": result}