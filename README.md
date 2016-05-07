# C0W0RK3R
*Find coworkers for your opensource projects!*

1. add "127.0.0.1 coworker.pythonanywhere.com" to your file "hosts"
2. create/copy  file "secret_settings.py" in "django_coworker" folder
   and "initial.py" in "django_coworker/fixtures"
3. python manage.py migrate
4. python manage.py loaddata initial
5. python manage.py createsuperuser
6. python manage.py runserver

**Go to http://coworker.pythonanywhere.com:8000 in your browser!**