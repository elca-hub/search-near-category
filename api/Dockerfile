FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
USER root

RUN apt-get update

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install -r requirements.txt