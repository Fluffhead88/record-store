from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Band(models.Model):
    date_formed = models.CharField(max_length=25, default="No date provided")
    city_origin = models.CharField(max_length=80, default="No city provided")
    genre = models.CharField(max_length=80, default="No genre provided")
    band_name = models.CharField(max_length=255)

class Album(models.Model):
    release_date = models.CharField(max_length=25, default="No date provided")
    title = models.CharField(max_length=255)
    tracks = models.CharField(max_length=400)
    genre = models.CharField(max_length=80)
    notes = models.TextField()
