from django.shortcuts import render
from .models import Song
from billing.models import Purchase
from django.contrib.auth.decorators import login_required

def song_catalog(request):
    songs = Song.objects.all()
    purchased_song_ids = []

    if request.user.is_authenticated:
        user_purchases = Purchase.objects.filter(user=request.user)
        purchased_song_ids = [purchase.song.id for purchase in user_purchases]

    return render(request, 'catalog/catalog.html', {'songs': songs, 'purchased_song_ids': purchased_song_ids})

@login_required(login_url='/accounts/login/')
def my_library(request):
    # Достаем все чеки текущего пользователя
    user_purchases = Purchase.objects.filter(user=request.user)
    # Вытаскиваем из чеков сами объекты песен
    purchased_songs = [purchase.song for purchase in user_purchases]
    
    return render(request, 'catalog/library.html', {'songs': purchased_songs})

