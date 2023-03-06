#!/bin/bash

NAME="ApiAutomateSUP"  # Nombre de la aplicación Django
DIR=/root/apis/apiSuscriptions/  # Directorio donde se encuentra el manage.py
USER=root  # El usuario con el que ejecutar gunicorn
GROUP=root  # El grupo con el que ejecutar gunicorn
WORKERS=3  # El número de workers que ejecutará gunicorn
BIND_IP=0.0.0.0  # La dirección IP en la que gunicorn escuchará las conexiones
BIND_PORT=8000  # El puerto en el que gunicorn escuchará las conexiones
DJANGO_SETTINGS_MODULE=ApiAutomateSUP.settings  # La ruta al archivo settings.py

# Activar el entorno virtual de python
source /root/apis/apiSuscriptions/suscriptionsenv/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DIR:$PYTHONPATH

# Ejecutar gunicorn
cd $DIR
exec /root/apis/apiSuscriptions/suscriptionsenv/bin/gunicorn ${NAME}.wsgi:application \
  --name $NAME \
  --workers $WORKERS \
  --bind $BIND_IP:$BIND_PORT \
  --user=$USER --group=$GROUP \
  --log-level=debug \
  --log-file=-
