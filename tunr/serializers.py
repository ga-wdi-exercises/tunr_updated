from rest_framework import serializers
from .models import Artist

class ArtistSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Artist
        fields = ('id', 'photo_url', 'nationality', 'name')