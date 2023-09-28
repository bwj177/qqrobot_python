FROM python:3.7

ENV PATH /usr/local/bin$PATH

ADD . /cqRobot


WORKDIR /cqRobot

RUN pip install -r requirements.txt