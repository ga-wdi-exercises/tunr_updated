from django.shortcuts import render, redirect
from .models import Artist, Song
from .forms import ArtistForm

# Create your views here.


def artist_list(request):
    artists = Artist.objects.all()
    return render(request, 'tunr/artist_list.html', {'artists': artists})


def artist_detail(request, pk):
    artist = Artist.objects.get(id=pk)
    return render(request, 'tunr/artist_detail.html', {'artist': artist})


def artist_create(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            artist = form.save()
            return redirect('artist_detail', pk=artist.id)
    else:
        form = ArtistForm()
    return render(request, 'tunr/artist_form.html', {'form': form})


def artist_edit(request, pk):
    artist = Artist.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArtistForm(request.POST, instance=artist)
        if form.is_valid():
            artist = form.save()
            return redirect('artist_detail', pk=artist.pk)
    else:
        form = ArtistForm(instance=artist)
    return render(request, 'tunr/artist_form.html', {'form': form})


def artist_delete(request, pk):
    Artist.objects.get(pk=pk).delete()
    return redirect('artist_list')


def song_detail(request, pk):
    song = Song.objects.get(id=pk)
    return render(request, 'tunr/song_detail.html', {'song': song})


def song_list(request):
    songs = Song.objects.all()
    return render(request, 'tunr/song_list.html', {'songs': songs})
