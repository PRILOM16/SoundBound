from django.urls import path
from . import views

urlpatterns = [
    path('', views.song_catalog, name='catalog'), 
    path('library/', views.my_library, name='my_library'),
    path('songs/<int:song_id>/delete/', views.delete_song, name='delete_song'),]