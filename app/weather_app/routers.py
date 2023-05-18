from fastapi import APIRouter

from app.sql_app.database import SessionLocal
from app.sql_app.models import WeatherReport

router = APIRouter()


def get_db(*args, **kwargs):
    return SessionLocal()


@router.get("/ping")
async def ping():
    return "pong!"


@router.post("/weather")
def show_weather():
    db = get_db()
    weather = db.query(WeatherReport).all()
    db.close()
    return weather
