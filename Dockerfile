FROM python:3.11-slim

RUN mkdir /code
WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
COPY .env ./code
ENV DATABASE_URL=postgres://postgres:password@todops:5432/mydb
CMD python todolist/manage.py runserver 0.0.0.0:8000