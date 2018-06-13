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
    
