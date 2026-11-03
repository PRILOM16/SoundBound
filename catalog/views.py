from django.shortcuts import render
from .models import Song
from billing.models import Purchase
from django.contrib.auth.decorators import login_required

def song_catalog(request):
    songs = Song.objects.filter(deleted_at__isnull=True)
    purchased_song_ids = []

    if request.user.is_authenticated:
        user_purchases = Purchase.objects.filter(user=request.user)
        purchased_song_ids = [purchase.song.id for purchase in user_purchases]

    return render(request, 'catalog/catalog.html', {'songs': songs, 'purchased_song_ids': purchased_song_ids})

@login_required(login_url='/accounts/login/')
def my_library(request):
    # Получаем все покупки текущего пользователя
    purchases = Purchase.objects.filter(user=request.user).select_related('song')

    return render(request, 'catalog/library.html', {
        'purchases': purchases
    })

