# Tarea 1 - IIC2173

## Requisitos

Para iniciar el programa es necesario tener instalado previamente:
- Python3.6
- virtualenv >=16.0.0
- Postgres >=9.4

## Setup

Iniciamos un nuevo ambiente con `virtualenv`, y luego lo activamos
```sh
virtualenv venv
. ./venv/bin/activate
```

Luego, instalamos los requisitos
```sh
pip install -r requirements.txt
```

Ahora configuramos la base de datos:
```sh
su -u postgres psql
$ create database iic2173t1;
```
Para después correr las migraciones:
```sh
python manage.py db update
```

Y finalmente corremos el servidor

```sh
python manage.py runserver
```

## Production

Para producción, descargaremos el repositorio, agregamos nuestras variables de entorno e iniciamos con `docker-compose`

```sh
git clone https://github.com/gsulloa/iic2173-t1.git server
cd server
touch .env
```

```env
# .env
DATABASE_URL=postgresql://postgres:@postgres/iic2173t1
SECRET_KEY=this-really-needs-to-be-changed
APP_SETTINGS=config.ProductionConfig
```

```sh
docker-compose build
docker-compose exec python manage.py upgrade
docker-compose up -d
```