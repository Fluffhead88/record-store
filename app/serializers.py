from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from app.models import Band, Album

class BandSerializer(ModelSerializer):

    class Meta:
        fields = "__all__"
        model = Band

class AlbumSerializer(ModelSerializer):

    class Meta:
        fields = "__all__"
        model = Album
