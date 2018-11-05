FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /retirement
WORKDIR /retirement
ADD . /retirement/
RUN pip install -r requirements.txt