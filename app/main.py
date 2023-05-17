import fastapi

from app.sql_app.database import Base, engine
from app.tools.helpers import run_loop
from app.weather_app.routers import router


def build_app() -> fastapi.FastAPI:
    Base.metadata.create_all(bind=engine)
    app = fastapi.FastAPI(
        title="TITLE",
        description="DESCRIPTION",
    )
    app.include_router(router)
    run_loop(app)
    return app
