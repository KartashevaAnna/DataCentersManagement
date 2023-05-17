from sqlalchemy import Float
from sqlmodel import Column, Integer, String

from app.sql_app.database import Base


class WeatherReport(Base):
    __tablename__ = "weather_report"

    id = Column(Integer, primary_key=True, index=True)
    city = Column(String)
    temperature = Column(Float)
    pressure = Column(Float)
    humidity = Column(Float)
    wind_speed = Column(Float)
    wind_gust = Column(Float)
