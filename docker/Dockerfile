FROM python:3
LABEL version="1.0.0" description="Disponibilizando site com Django" maintainer="Daniel F. Schulz<danielschulz@bb.com.br>"
WORKDIR /code
COPY . /code
RUN mkdir /usr/share/nltk
COPY ./packages/punkt ./packages/stopwords /usr/share/nltk/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
