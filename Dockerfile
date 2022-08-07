FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /Django-CRUD-Project
RUN pip install -r reqirements.txt
COPY . /docker