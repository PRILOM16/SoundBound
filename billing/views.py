from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Purchase
from catalog.models import Song

@login_required
def buy_song(request, song_id):
    if request.method == 'POST':
        song = get_object_or_404(Song, id = song_id)

        Purchase.objects.create(user=request.user, song=song)

        return redirect('catalog')

    return redirect('catalog')
