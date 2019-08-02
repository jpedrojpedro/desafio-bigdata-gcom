FROM python:3-alpine

LABEL maintainer="João Pedro Pinheiro <joaopedro.pinheiro88@gmail.com>"

RUN apk add --no-cache bash

RUN pip3 install --no-cache-dir --upgrade pip \
 && pip3 install Flask==1.1.1                 \
                 peewee==3.9.6                \
                 requests==2.22.0             \
                 beautifulsoup4==4.8.0
