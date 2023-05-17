import fastapi

from app.sql_app.database import engine, Base
from app.weather_app.routers import router


# load_dotenv()
#
# #CITIES = {"Tokyo", "Delhi", "Shanghai"}
# CITIES = {"Shanghai"}
# '''Took cities from https: // en.wikipedia.org / wiki / List_of_largest_cities. '''
# APIKEY = os.getenv("OPENWEATHERAPIKEY")
#
# models.Base.metadata.create_all(bind=engine)
#
# app = FastAPI()
#
#
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


#
#
#
# # @app.get("/")
# # async def root():
# #     return {"message": "Hello World"}
#
#
# async def api_key():
#     print(APIKEY)
#
#
# async def get_cities():
#     res = []
#     for city in CITIES:
#         res.append(city)
#     print(res)
#
#
# res = []
#
#
#
# async def get_weather():
#     async with httpx.AsyncClient() as client:
#         for city in CITIES:
#             url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={APIKEY}&units=metric"
#             response = await client.get(url)
#             res.append(response.text)
#
#     print(res)
#     return res
#
#
# # router = APIRouter()
# # @router.post("/cities")
# async def create_city(city: str):
#     db = SessionLocal()
#     db.add(models.WeatherReport(city=city, temperature="34,7"))
#     db.commit()
#     cities = db.query(models.WeatherReport).all()
#     db.close()
#     print(cities)


# app = FastAPI()
def build_app() -> fastapi.FastAPI:
    Base.metadata.create_all(bind=engine)
    app = fastapi.FastAPI(
        title="TITLE",
        description="DESCRIPTION",
    )
    app.include_router(router)
    return app


# @app.on_event("startup")
# # @repeat_every(seconds=60 * 60)
# # @repeat_every(seconds=3)
# async def recurring_function():
#     await asyncio.gather(
#         get_cities(),
#         # create_city(),
#         # init_db(),
#         # create_city(),
#
#         # api_key(),
#         # get_cities(),
#         # get_weather(),
#     )
