FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /retirement
RUN apt-get update && apt-get install -y python-dev libldap2-dev libsasl2-dev libssl-dev
WORKDIR /retirement
ADD . /retirement/
RUN pip install -r requirements.txt