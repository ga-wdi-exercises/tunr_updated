from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArtistList.as_view(), name='artist_list'),
    path('songs/', views.SongList.as_view(), name='song_list'),
    path('artists/<int:pk>', views.artist_detail, name='artist_detail'),
    path('songs/<int:pk>', views.SongDetail.as_view(), name='song_detail'),
    path('artists/new', views.ArtistCreate.as_view(), name='artist_create'),
    path('songs/new', views.SongCreate.as_view(), name='song_create'),
    path('artists/<int:pk>/edit', views.artist_edit, name='artist_edit'),
    path('songs/<int:pk>/edit', views.SongEdit.as_view(), name='song_edit'),
    path('artists/<int:pk>/delete', views.ArtistDelete.as_view(), name='artist_delete'),
    path('songs/<int:pk>/delete', views.SongDelete.as_view(), name='song_delete'),
]
