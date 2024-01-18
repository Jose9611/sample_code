#!/bin/sh

# Wait for PostgreSQL to be ready
echo "Waiting for PostgreSQL..."
dockerize -wait tcp://db:5432 -timeout 60s

# Wait for Redis to be ready
echo "Waiting for Redis..."
dockerize -wait tcp://redis:6379 -timeout 60s

# Run Django migrations and start the application
python manage.py migrate
python manage.py runserver 0.0.0.0:8000

exec "$@"
