from rest_framework.generics import ListCreateAPIView
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Song
from rest_framework.pagination import PageNumberPagination
from .serializers import SongSerializer
from albums.models import Album

import ipdb


class SongView(ListCreateAPIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Song.objects.all()
    serializer_class = SongSerializer

    def get_queryset(self):
        # ipdb.set_trace()
        id_album = self.kwargs['pk']
        queryset = Song.objects.get(album=id_album)
        return self.queryset

    def perform_create(self, serializer):
        return serializer.save(album_id=self.kwargs.get('pk'))
