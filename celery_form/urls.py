from django.urls import path

from .views import note_form


app_name = 'celery_form'
urlpatterns = [
    path('', note_form, name='index'),
]
