#!/usr/bin/env bash
# exit on error
set -o errexit

#poetry install para no usar poestry
#pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate