FROM nginx:1.19.0-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/nginx.conf

RUN mkdir /usr/src
RUN mkdir /usr/src/backend
RUN mkdir /usr/src/backend/static