import uvicorn

from main import build_app


def main():
    uvicorn.run(
        build_app(),
        host="127.0.0.1",
        port=8000,
    )


if __name__ == "__main__":
    main()
