FROM python:3.11-slim

WORKDIR /opt
COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["bash", "makemigrations.sh"]

EXPOSE 8000

CMD ["gunicorn", "todolist.wsgi", "-w", "4", "-b", "0.0.0.0.8000"]

#ENV DATABASE_URL=postgres://postgres:password@todops:5432/mydb
#CMD python todolist/manage.py runserver 0.0.0.0:8000