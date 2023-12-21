cd mobi_market; python manage.py collectstatic --no-input; python manage.py migrate; gunicorn mobi_market.wsgi:application -w 4 -b 0.0.0.0:8000;
