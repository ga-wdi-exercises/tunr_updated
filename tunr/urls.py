from django.urls import path
from . import views

urlpatterns = [
    path('artists/', views.ArtistList.as_view(), name='artist_list'),
    path('artists/<int:pk>', views.ArtistDetail.as_view(), name='artist_detail'),
    # path('songs/<int:pk>', views.song_detail, name='song_detail')
]