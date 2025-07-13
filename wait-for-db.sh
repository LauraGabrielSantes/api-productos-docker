#!/bin/sh
echo "Esperando a que la base de datos esté lista..."
while ! nc -z db 3306; do  #usa el comando netcat para verificar si el puerto 3306 en el host db está abierto
  sleep 1
done
echo "Base de datos disponible. Iniciando backend..."
exec "$@" #Ejecuta el comando que se haya pasado como argumento al script, reemplazando el proceso actual