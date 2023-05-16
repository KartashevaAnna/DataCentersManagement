from sqlmodel import Column, Integer, String
from app.sql_app.database import Base


class WeatherReport(Base):
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, index=True)
    city = Column(String)
    temperature = Column(String)