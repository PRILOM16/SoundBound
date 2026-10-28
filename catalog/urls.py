from django.urls import path
from . import views

urlpatterns = [
    path('', views.song_catalog, name='catalog'), 
]