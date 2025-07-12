#!/bin/sh

echo "Waiting for PostgreSQL..."

while ! nc -z db 5432; do
  sleep 1
done

echo "PostgreSQL is ready!"

# Apply migrations and collectstatic
python manage.py migrate
python manage.py collectstatic --noinput

# Start Gunicorn
exec gunicorn school_one.wsgi:application --bind 0.0.0.0:8000
