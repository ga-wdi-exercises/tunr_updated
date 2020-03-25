from django.urls import path
from . import views

urlpatterns = [
    # Artist
    path('artists/', views.ArtistList.as_view(), name='artist_list'),
    path('artists/<int:pk>', views.ArtistDetail.as_view(), name='artist_detail'),
    # Songs
    path('songs/', views.song_list, name='song_list'),
    path('songs/<int:pk>', views.song_detail, name='song_detail'),
    path('songs/new', views.song_create, name='song_create'),
    path('songs/<int:pk>/edit', views.song_edit, name='song_edit'),
    path('songs/<int:pk>/delete', views.song_delete, name='song_delete'),
]
