from django.shortcuts import render, redirect
from rest_framework import generics
from .serializers import ArtistSerializer
from .models import Artist
from rest_framework import permissions

class ArtistList(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = (permissions.IsAuthenticated,)

class ArtistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = (permissions.IsAuthenticated,)
