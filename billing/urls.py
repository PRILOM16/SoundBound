from django.urls import path
from . import views

app_name = 'billing'

urlpatterns = [
    path('buy/<int:song_id>/', views.buy_song, name='buy_song')
]