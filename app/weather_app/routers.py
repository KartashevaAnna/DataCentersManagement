from fastapi import APIRouter
from fastapi.responses import PlainTextResponse

from app.sql_app.database import SessionLocal
from app.sql_app.models import WeatherReport

router = APIRouter()


def get_db(*args, **kwargs):
    return SessionLocal()


@router.get("/ping", response_class=PlainTextResponse)
async def ping():
    """Healthcheck"""

    return "pong!"


@router.post("/weather")
def show_weather():
    """Returns database content."""

    db = get_db()
    weather = db.query(WeatherReport).all()
    db.close()
    return weather
