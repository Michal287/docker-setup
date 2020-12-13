# shop_api

Shop project which using Django(DRF)+React+Docker+Nginx+Gunicorn+PostgreSQL

# How to run
### You need to create folder "config" and then put 2 files in it:

django_settings

```shell
DEBUG= 
SECRET_KEY= 
SQL_ENGINE=
SQL_DATABASE=
SQL_USER=
SQL_PASSWORD=
SQL_HOST=
SQL_PORT=
```

database_env

```shell
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_DB=
```
### Next step is to build images

```shell
sudo docker-compose build
```

### The last step is run a server

```shell
sudo docker-compose up -d
```

