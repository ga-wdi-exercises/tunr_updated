from django.urls import path
from . import views

urlpatterns = [
    # Artist
    path('artists/', views.ArtistList.as_view(), name='artist_list'),
    path('artists/<int:pk>', views.ArtistDetail.as_view(), name='artist_detail'),
    # Songs
    path('songs/', views.SongList.as_view(), name='song_list'),
    path('songs/<int:pk>', views.SongDetail.as_view(), name='song_detail')
]
