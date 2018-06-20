from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from django_filters.rest_framework import DjangoFilterBackend
from app.models import Band, Album
from app.serializers import BandSerializer, AlbumSerializer
from app.permissions import IsOwnerOrReadOnly


class BandListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = BandSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Band.objects.all()

        return Band.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class BandRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = BandSerializer

    def get_queryset(self):
        return Band.objects.filter(user=self.request.user)


class AlbumListCreateAPIView(APIView):

    def get(self, request):
        all_albums = self.get_queryset()
        serialized_albums = AlbumSerializer(all_albums, many=True)
        return Response(serialized_albums.data, 200)

    def get_queryset(self):
        queryset = Album.objects.all()
        title = self.request.query_params.get('title')
        band = self.request.query_params.get('band')
        if title:
            queryset = queryset.filter(title=title)
        if band:
            queryset = queryset.filter(band_id=band)

        return queryset

    def post(self, request):
        permission_classes = [IsOwnerOrReadOnly]
        owner = self.request.user
        band_id = request.POST.get('band', None)
        user_id = request.POST.get('user', None)
        release_date = request.POST['release_date']
        title = request.POST['title']
        tracks = request.POST['tracks']
        genre = request.POST['genre']
        notes = request.POST['notes']
        new_album = Album.objects.create(
            release_date=release_date, title=title, tracks=tracks, genre=genre, notes=notes)
        serialized_album = AlbumSerializer(new_album)
        return Response(serialized_album.data, 201)


class AlbumDetailAPIView(APIView):
    def get(self, request, pk):
        album = Album.objects.get(id=pk)
        serialized_album = AlbumSerializer(album)
        return Response(serialized_album.data, 200)

    def put(self, request, pk):
        permission_classes = [IsOwnerOrReadOnly]
        user = self.request.user
        album = Album.objects.get(id=pk)
        album.band_id = request.POST.get('band', None)
        album.user_id = request.POST.get('user', None)
        album.release_date = request.POST['release_date']
        album.title = request.POST['title']
        album.tracks = request.POST['tracks']
        album.genre = request.POST['genre']
        album.notes = request.POST['notes']
        album.save()
        serialized_album = AlbumSerializer(album)
        return Response(serialized_album.data, 200)

    def delete(self, response, pk):
        permission_classes = [IsOwnerOrReadOnly]
        user = self.request.user
        album = Album.objects.get(id=pk)
        album.delete()
        return Response("", 204)


"""class AlbumListView(generics.ListAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title', 'tracks', 'genre')"""
