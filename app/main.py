import fastapi

from app.sql_app.database import Base, engine
from app.tools.helpers import run_loop
from app.weather_app.routers import router


def build_app() -> fastapi.FastAPI:
    """Build application."""

    Base.metadata.create_all(bind=engine)
    app = fastapi.FastAPI(
        title="Weather collector",
        description="Collects weather reports for 50 largest cities",
    )
    app.include_router(router)
    run_loop(app)
    return app
