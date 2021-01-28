FROM python:3
LABEL version="1.0.0" description="Disponibilizando site com Django" maintainer="Daniel F. Schulz<danielschulz@bb.com.br>"
WORKDIR /code
COPY . /code
COPY ./packages/punkt/ /usr/share/nltk_data/tokenizers
COPY ./packages/stopwords/ /usr/share/nltk_data/corpora
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
