# Dockerfile

# pull the official docker image
FROM python:3.9-slim-buster

# set work directory
WORKDIR /usr/src/app

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# OS Dependencies
RUN apt-get update \
    && apt-get install -y build-essential \
    && apt install -y curl


# install dependencies
RUN pip install --upgrade pip
COPY ./app/requirements.txt .
RUN pip install -r requirements.txt


# copy entrypoint.sh
COPY ./app/entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh


# copy project
COPY ./app .
COPY .env .

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]