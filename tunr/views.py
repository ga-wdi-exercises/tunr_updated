from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views import View
from django.urls import reverse_lazy

from .models import Artist, Song
from .forms import ArtistForm, SongForm

class ArtistList(View):
    def get(self, request):
        artists = Artist.objects.all()
        return render(request, 'tunr/artist_list.html', {'artists': artists})

class ArtistCreate(View):
    form_class = ArtistForm
    template_name = 'tunr/artist_form.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            artist = form.save()
            return redirect('artist_detail', pk=artist.pk)

        return render(request, self.template_name, {'form': form})

def artist_edit(request, pk):
    artist = Artist.objects.get(pk=pk)
    if request.method == "POST":
        form = ArtistForm(request.POST, instance=artist)
        if form.is_valid():
            artist = form.save()
            return redirect('artist_detail', pk=artist.pk)
    else:
        form = ArtistForm(instance=artist)
    return render(request, 'tunr/artist_form.html', {'form': form})

def artist_detail(request, pk):
    artist = Artist.objects.get(id=pk)
    return render(request, 'tunr/artist_detail.html', {'artist': artist})

class ArtistDelete(DeleteView):
    model = Artist
    success_url = reverse_lazy('song_list')

class SongList(ListView):
    model = Song
    context_object_name = 'songs'

class SongDetail(DetailView):
    queryset = Song.objects.all()
    context_object_name = 'song'

class SongCreate(CreateView):
    model = Song
    fields = ('title', 'album', 'preview_url', 'artist')

class SongEdit(UpdateView):
    model = Song
    fields = ('title', 'album', 'preview_url', 'artist')

class SongDelete(DeleteView):
    model = Song
    success_url = reverse_lazy('song_list')