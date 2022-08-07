FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /docker
COPY reqirements.txt /docker/
RUN pip install -r reqirements.txt
COPY . /docker