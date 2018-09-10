FROM tiangolo/uwsgi-nginx-flask:python3.6

RUN rm /app/prestart.sh


COPY requirements.txt /tmp/
RUN pip install -U pip
RUN pip install -r /tmp/requirements.txt

COPY ./main.py /app
COPY ./config.py /app
COPY ./manage.py /app
COPY ./models.py /app
COPY ./templates /app/templates
COPY ./migrations /app/migrations