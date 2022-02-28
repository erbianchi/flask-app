FROM python:3.8-slim-buster

WORKDIR /usr/src/app

COPY application.py .
COPY requirements.txt .
COPY static static
COPY templates templates

RUN pip install -r requirements.txt

EXPOSE 8080

ENV FLASK_APP=application.py
ENV PYTHONPATH="/usr/src/app"

CMD ["twistd", "--no_save", "--nodaemon", "web", "-n", "--port", "tcp:8080", "--wsgi", "application.app"]
