FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN python3 -m pip install -r requirements.txt
COPY . /Django-CRUD-Project