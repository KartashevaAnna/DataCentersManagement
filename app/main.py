import fastapi

from weather.sql_app.database import engine, Base
from weather.tools.helpers import run_loop
from weather.weather_app.routers import router


def build_app() -> fastapi.FastAPI:
    Base.metadata.create_all(bind=engine)
    app = fastapi.FastAPI(
        title="TITLE",
        description="DESCRIPTION",
    )
    app.include_router(router)
    run_loop(app)
    return app
