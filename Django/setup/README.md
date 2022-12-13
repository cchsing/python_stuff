# Setup related commands, scripts, and configurations

1. pip install django==2.0.7
2. django-admin
   - django-admin create
3. python manage.py runserver 0.0.0.0:8000
   - running at 127.0.0.1:8000 seems problematic as the localhost address does not loop to the hostname and host ip
4. Edit the setting in settings.py to allow access from client browser
   - `ALLOWED_HOSTS = ["server_hostname","server_ip"]`
5. python manage.py createsuperuser
6. python manage.py migrate
