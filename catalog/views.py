from django.shortcuts import render
from .models import Song

def song_catalog(request):
    songs = Song.objects.all()

    return render(request, 'catalog/catalog.html', {'songs': songs})
