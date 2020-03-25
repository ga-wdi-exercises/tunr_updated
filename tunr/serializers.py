from rest_framework import serializers
from .models import Artist, Song

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    songs = serializers.HyperlinkedRelatedField(
        view_name='song_detail',
        many=True,
        read_only=True
    )

    artist_url = serializers.ModelSerializer.serializer_url_field(
        view_name='artist_detail'
    )

    class Meta:
        model = Artist
        fields = ('id', 'photo_url', 'nationality', 'name', 'songs', 'artist_url')

class SongSerializer(serializers.HyperlinkedModelSerializer):
    artist = serializers.HyperlinkedRelatedField(
        view_name='artist_detail',
        read_only=True
    ) 

    artist_id = serializers.PrimaryKeyRelatedField(
        queryset=Artist.objects.all(),
        source='artist'
    )

    class Meta:
        model = Song
        fields = ('id', 'artist', 'artist_id', 'title', 'album', 'preview_url')
