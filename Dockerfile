FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /app/logs
WORKDIR /app
COPY ./requirements/base.txt /app/
RUN pip install -r base.txt
RUN apt-get update
RUN apt-get install nano
ARG CACHEBUST
COPY . /app/
RUN python3 manage.py collectstatic --noinput
RUN python3 manage.py makemigrations
RUN python3 manage.py migrate
RUN python3 manage.py init_admin