from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=250)
    artist = models.CharField(max_length=250)
    year = models.IntegerField()
    price = models.FloatField()

    demo_audio = models.FileField(upload_to='songs/demo/')
    full_audio = models.FileField(upload_to='songs/full/')

    def __str__(self):
        return f"{self.artist} - {self.title} ({self.year})"