# Tarea 1 - IIC2173

## Requisitos

Para iniciar el programa es necesario tener instalado previamente:
- virtualenv >=16.0.0

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

Y corremos el servidor

```sh
FLASK_APP=index.py flask run
```