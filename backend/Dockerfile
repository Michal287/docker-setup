FROM python:3.8.5

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y --no-install-recommends postgresql-client

# arbitrary location
RUN mkdir -p /var/backend
WORKDIR /var/backend

# install our dependencies
COPY requirements.txt /var/backend
RUN pip install -r requirements.txt

# copy our project code
COPY . /var/backend

ENTRYPOINT ["sh", "entrypoint.sh"]