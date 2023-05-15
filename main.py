import copy
import os
import asyncio
from fastapi import FastAPI
from fastapi_utils.tasks import repeat_every
from dotenv import load_dotenv

CITIES = {"Tokyo", "Delhi", "Shanghai"}

load_dotenv()

OPENWEATHERAPIKEY = os.getenv("OPENWEATHERAPIKEY")

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


async def print_hello():
    print("HELLO!")


async def second_hello():
    print("hi!")


async def api_key():
    print(OPENWEATHERAPIKEY)


async def get_cities():
    '''Took cities from https: // en.wikipedia.org / wiki / List_of_largest_cities. '''
    res = []
    for city in CITIES:
        res.append(city)
    print(res)


@app.on_event("startup")
# @repeat_every(seconds=60 * 60)
@repeat_every(seconds=3)
async def recurring_function():
    await asyncio.gather(
        print_hello(),
        second_hello(),
        api_key(),
        get_cities()
    )


