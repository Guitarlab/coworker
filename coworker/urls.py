from django.conf.urls import url
from . import views

app_name = 'coworker'
urlpatterns = [
    url(r'^choose_project/', views.choose_project, name='choose_project')
]
