from python:3

COPY requirements.txt ./

RUN pip install -r requirements.txt

ENV SHELL /bin/bash