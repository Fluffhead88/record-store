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

    def __str__(self):
        return self.band_name


class Album(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default = 0)
    release_date = models.CharField(max_length=25, default="No date provided")
    title = models.CharField(max_length=255)
    tracks = models.CharField(max_length=400)
    genre = models.CharField(max_length=80)
    notes = models.TextField()
    band = models.ForeignKey(Band, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    #def albums(self):
    #    return self.album_set.count()
