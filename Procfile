release: python manage.py makemigrations && python manage.py migrate
web: gunicorn socialweb.wsgi --log-file -
