FROM schulzdaniel/django
ENV PYTHONUNBUFFERED=1
MAINTAINER DANIEL SCHULZ
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code
