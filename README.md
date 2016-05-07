#coworker
*Find coworkers for your opensource projects!*

1. add to file "hosts":  127.0.0.1 coworker.pythonanywhere.com
2. create/copy  file "secret_settings.py" in "django_coworker" folder
3. python manage.py migrate
4. python manage.py loaddata initial
5. python manage.py runserver

**Go to "http://coworker.pythonanywhere.com:8000" in your browser!**