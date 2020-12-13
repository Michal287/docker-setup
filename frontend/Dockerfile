FROM node:10

RUN mkdir -p /var/frontend
WORKDIR /var/frontend

COPY . /var/frontend

RUN apt-get update
RUN apt-get -y install curl gnupg
RUN curl -sL https://deb.nodesource.com/setup_10.x  | bash -
RUN apt-get -y install nodejs
RUN npm install
RUN npm install -g serve
