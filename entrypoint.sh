#!/bin/bash
set -e

echo "Applying database migrations..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput

python criar_dicionario.py

echo "Starting server..."
exec "$@"
