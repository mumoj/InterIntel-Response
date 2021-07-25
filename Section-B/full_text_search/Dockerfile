# syntax = docker/dockerfile:1.2 # Enable BUILDKIT caching.
# pull official base image
FROM python:3.6-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# Install uWSGI server dependencies
RUN apk update \
    && apk add linux-headers pcre-dev

# install Django dependencies and cache them
COPY ./requirements.txt .
RUN --mount=type=cache,target=/root/.cache \
    pip  install -r requirements.txt

# create directory for the app user
RUN mkdir -p /home/app

# create the app user
RUN addgroup -S app && adduser -S app -G app

# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME

# create staticfiles folder
RUN mkdir $APP_HOME/staticfiles 
WORKDIR $APP_HOME

# Copy Django project.
COPY . $APP_HOME

# copy entrypoint.sh
COPY ./entrypoint.sh $APP_HOME

# chown all the files to the app user
RUN chown -R app:app $APP_HOME

# change to the app user
USER app

# run entrypoint.sh
ENTRYPOINT ["/home/app/web/entrypoint.sh"]




