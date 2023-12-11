from django.shortcuts import get_object_or_404, render
from .models import Albums, Songs

def albums(request):
    albums = Albums.objects.all()
    return render(request,
                  'reviews/albums.html',
                  {'albums':albums})

def album_view(request, album):
    songs = Songs.objects.filter(album=album)
    return render(request,
                  'reviews/album_view.html',
                  {'songs':songs})

def song_view(request, slug):
    song = get_object_or_404(Songs,
                              slug=slug)
    length_min = str(song.length // 60)
    length_sec = str(song.length % 60)
    song_contains_seconds = length_sec != 0
    # Context
    context = {
        'song':song,
        'length_min':length_min,
        'length_sec':length_sec,
        'song_contains_seconds':song_contains_seconds,
    }
    return render(request,
                  'reviews/song.html',
                  context)
