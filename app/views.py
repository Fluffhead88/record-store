from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from app.models import Band, Album
from app.serializers import BandSerializer, AlbumSerializer
from app.permissions import IsOwnerOrReadOnly

class BandListCreateAPIView(generics.ListCreateAPIView):
    queryset = Band.objects.all()
    serializer_class = BandSerializer

class BandRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    permisison_classes = [IsOwnerOrReadOnly]
    queryset = Band.objects.all()
    serializer_class = BandSerializer

class AlbumListCreateAPIView(APIView):
    def get(self, request):
        all_albums = Album.objects.all()
        serialized_albums = AlbumSerializer(all_albums, many=True)
        return Response(serialized_albums.data, 200)

    def post(self, request):
        user = self.request.user
        release_date = request.POST['release_date']
        title = request.POST['title']
        tracks = request.POST['tracks']
        genre = request.POST['genre']
        notes = request.POST['notes']
        new_album = Album.objects.create(release_date=release_date, title=title, tracks=tracks, genre=genre, notes=notes)
        serialized_album = AlbumSerializer(new_album)
        return Response(serialized_album.data, 201)

class AlbumDetailAPIView(APIView):
    def get(self, request, pk):
        album = Album.objects.get(id=pk)
        serialized_album = AlbumSerializer(album)
        return Response(serialized_album.data, 200)

    def put(self, request, pk):
        album = Album.objects.get(id=pk)
        album.release_date = request.POST['release_date']
        album.title = request.POST['title']
        album.tracks = request.POST['tracks']
        album.genre = request.POST['genre']
        album.notes = request.POST['notes']
        album.save()
        serialized_album = AlbumSerializer(album)
        return Response(serialized_album.data, 200)

    def delete(self, response, pk):
        album = Album.objects.get(id=pk)
        album.delete()
        return Response("", 204)
