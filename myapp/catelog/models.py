from django.db import models

# Create your models here.

class album(models.Model):
    albumName = models.CharField(max_length=100,unique=True)
    albumArtist = models.CharField(max_length=100,unique=False)
    albumRealeaseYear = models.CharField(max_length=100,unique=False)
    albumCover = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)

    def __str__(self):
        return self.albumName

class song(models.Model):
    songName = models.CharField(max_length=100,unique=True)
    songDuration = models.CharField(max_length=100,unique=False)

    def __str__(self):
        return self.songName

class awards(models.Model):
    awardName = models.CharField(max_length=100,unique=True)
    dateOfAward = models.CharField(max_length=100,unique=False)

    def __str__(self):
        return self.awardName


    
