FROM python:3.9-slim

ENV PYTHONPATH=/app
ENV COVERAGE_FILE=/app/.coverage
ENV IN_DOCKER=1

RUN apt-get update && apt-get install git -y
RUN mkdir /app
WORKDIR /app

COPY ./requirements.txt ./dev-requirements.txt /app/
RUN pip install -r /app/requirements.txt -r /app/dev-requirements.txt
