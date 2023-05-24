FROM python:3.11 as base

FROM base AS os-dep
RUN apt-get update -y --fix-missing
RUN apt update -y --fix-missing
RUN apt-get -y install nano
RUN apt-get upgrade -y
ENV PYTHONUNBUFFERED=1
RUN pip install --upgrade pip
ARG CACHEBUST

FROM os-dep AS django-dep
WORKDIR /app/logs
WORKDIR /app
ENV PYTHONUNBUFFERED=2
COPY requirements/ /app/requirements/
RUN pip install -r ./requirements/base.txt
RUN pip install -r ./requirements/production.txt
ENV PYTHONUNBUFFERED=3
ARG CACHEBUST

FROM django-dep AS django
COPY core/ /app/core/
COPY configuration/ /app/configuration/
COPY backend/ /app/backend/
RUN python3 manage.py collectstatic --noinput
ARG CACHEBUST

ARG RUN_ENV
ENV RUN_ENV $RUN_ENV
ARG DATABASE_HOST
ENV DATABASE_HOST $DATABASE_HOST
ARG DATABASE_DOCKER_HOST
ENV DATABASE_DOCKER_HOST $DATABASE_DOCKER_HOST
ENV DATABASE_PORT=5432
ENV DATABASE_NAME=AnimalTrack
ENV DATABASE_USER=animal
ENV DATABASE_PASSWORD=password

COPY entrypoint.sh bin/entrypoint.sh
RUN chmod +x bin/entrypoint.sh

ENTRYPOINT ["bin/entrypoint.sh"]