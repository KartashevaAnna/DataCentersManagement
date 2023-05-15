import asyncio
from fastapi import FastAPI
from fastapi_utils.tasks import repeat_every

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


async def print_hello() -> None:
    print("HELLO!")


async def second_hello() -> None:
    print("hi!")


@app.on_event("startup")
@repeat_every(seconds=60 * 60)
# @repeat_every(seconds=3)
async def recurring_function() -> None:
    await asyncio.gather(print_hello(), second_hello())



