from django.db import models

class album(models.Model):
    albumName = models.CharField(max_length=100,unique=True)
    albumArtist = models.CharField(max_length=100,unique=False)
    albumRealeaseYear = models.CharField(max_length=100,unique=False)
    albumCover = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    songs = models.ManyToManyField('song', related_name='albums')
    awards = models.ManyToManyField('awards', related_name='albums')

    def __str__(self):
        return self.albumName

class song(models.Model):
    songTitle = models.CharField(max_length=100,unique=True)
    songDuration = models.CharField(max_length=100,unique=False)

    def __str__(self):
        return self.songTitle

class awards(models.Model):
    awardName = models.CharField(max_length=100,unique=True)
    dateOfAward = models.CharField(max_length=100,unique=False)
    
    def __str__(self):
        return self.awardName
