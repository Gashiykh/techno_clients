#!/bin/sh
set -e

until nc -z "$POSTGRES_HOST" "$POSTGRES_PORT"; do
  echo "Ждем подключения к PostgreSQL..."
  sleep 1
done

echo "=== Запуск миграций ==="
python manage.py migrate --noinput

echo "=== Запуск сервера ==="
gunicorn core.wsgi:application --bind 0.0.0.0:8001 --workers 3