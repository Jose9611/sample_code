#!/bin/bash

# Apply database migrations
python manage.py migrate

# Start the Django application
exec "$@"
