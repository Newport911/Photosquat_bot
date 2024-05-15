FROM python:3.8.10-slim

RUN mkdir docker_demo
WORKDIR docker_demo

ADD requirements.txt /docker_demo/
RUN pip install -r requirements.txt
ADD . /docker_demo/

RUN pip3 install -r requirements.txt


CMD python Final_Bot.py