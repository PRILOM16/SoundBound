from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=250)
    artist = models.CharField(max_length=250)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    demo_audio = models.FileField(upload_to='songs/demo/')
    full_audio = models.FileField(upload_to='songs/full/')

    deleted_at = models.DateField(
        null=True,
        blank=True,
        default=None)

    def __str__(self):
        return f"{self.artist} - {self.title} ({self.year})"