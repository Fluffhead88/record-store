from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Band(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    date_formed = models.CharField(max_length=25, default="No date provided")
    city_origin = models.CharField(max_length=80, default="No city provided")
    genre = models.CharField(max_length=80, default="No genre provided")
    band_name = models.CharField(max_length=255)
    #created = models.DateTimeField(auto_now_add=True)

    #def albums(self):
    #    return self.album_set.count()

class Album(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    band = models.ForeignKey(Band, null= True, on_delete=models.CASCADE)
    #created = models.DateTimeField(auto_now_add=True)
    release_date = models.CharField(max_length=25, default="No date provided")
    title = models.CharField(max_length=255)
    tracks = models.CharField(max_length=400)
    genre = models.CharField(max_length=80)
    notes = models.TextField()
