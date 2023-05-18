import uvicorn

from app.main import build_app


def main():
    uvicorn.run(
        "__main__:build_app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        forwarded_allow_ips="*",
    )


if __name__ == "__main__":
    main()
