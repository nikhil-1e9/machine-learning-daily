release: python manage.py collectstatic --noinput
web: gunicorn dswebsite.wsgi:application --log-file -