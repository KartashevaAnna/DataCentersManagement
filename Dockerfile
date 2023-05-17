FROM python:3.11-slim

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app

RUN python3 -m pip install --upgrade pip
RUN pip install -r /app/requirements.txt --no-cache-dir


COPY app/ /app

CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "15400" ]