from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from app.models import Band, Album

class BandSerializer(ModelSerializer):

    #albums = serializers.IntegerField()

    class Meta:
        fields = "__all__"
        read_only_fields = ["user"]
        model = Band

class AlbumSerializer(ModelSerializer):

    class Meta:
        fields = "__all__"
        read_only_fields = ["user", "band"]
        model = Album
