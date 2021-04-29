FROM ubuntu:18.04

COPY requirements.txt requirements.txt
RUN apt-get update
RUN apt-get install -y fortune
RUN apt-get install -y cowsay
RUN apt-get install -y python3.8
RUN apt-get install -y python3-pip

COPY . .

RUN pip3 install -r requirements.txt

ENV PATH=$PATH:/usr/games
ENV FLASK_APP=appserver.py
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8



CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0" ]
