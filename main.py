from fastapi import FastAPI
from fastapi_utils.tasks import repeat_every

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


def print_hello() -> None:
    print("HELLO!")


@app.on_event("startup")
@repeat_every(seconds=60 * 60)
def recurring_function() -> None:
    print_hello()
