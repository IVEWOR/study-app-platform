FROM python:3.9-alpine
LABEL maintainer="Deepslog Corporations"
LABEL email="howdy@deepslog.com"
LABEL website="deepslog.com"


ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user
