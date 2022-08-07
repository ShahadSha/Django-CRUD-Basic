FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /Django-CRUD-Project

COPY requirements.txt /Django-CRUD-Project/
RUN pip install -r requirements.txt

COPY . /Django-CRUD-Project