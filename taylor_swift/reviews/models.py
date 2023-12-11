from django.db import models
from django.urls import reverse

class Songs(models.Model):

    class Meta:
        ordering = ['-album']

    class Collaboration(models.TextChoices):
        COLLAB = 'C', "Collaboration"
        SINGLE = 'S', "Single"

    # Fields
    title = models.TextField(max_length=100)
    album = models.TextField(max_length=100)
    length = models.IntegerField()
    
    rating = models.FloatField()
    collab = models.TextField(max_length=1,
                              choices=Collaboration.choices,
                              default=Collaboration.SINGLE)
    slug = models.SlugField(max_length=200)
    link = models.TextField(max_length=500,
                            default="")


    def __str__(self) -> str:
        return self.title + 'from' + self.album

    def get_absolute_url(self):
        return reverse('reviews:song_view',
                       args=[self.slug])

class Albums(models.Model):

    class Meta:
        ordering = ['-publish']

    # Fields
    title = models.TextField(max_length=100)
    publish = models.DateField()
    cover = models.TextField(default="https://www.charitycomms.org.uk/wp-content/uploads/2019/02/placeholder-image-square.jpg")

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('reviews:album_view',
                       args=[self.title])
