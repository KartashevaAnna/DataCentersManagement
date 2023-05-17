import asyncio
from typing import Annotated

import uvicorn
from fastapi import Depends

from app.main import build_app
from app.weather_app.routers import get_weather_report


def main():
    uvicorn.run(
        build_app(),
        host="127.0.0.1",
        port=8000,
    )


if __name__ == "__main__":
    main()
