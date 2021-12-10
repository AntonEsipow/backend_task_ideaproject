from django.db import models
from django.urls import reverse


class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('image_detail', args=[str(self.pk)])
