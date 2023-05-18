FROM python:3.11


WORKDIR /usr/src/app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt


COPY . /usr/src/app

CMD python3.11 run.py