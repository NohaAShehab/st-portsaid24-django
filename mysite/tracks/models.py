from django.db import models
from django.shortcuts import reverse

# Create your models here.


class Track(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=500)
    logo = models.ImageField(upload_to='tracks/logos', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name

    @property
    def show_url(self):
        url = reverse('tracks.show', args=[self.id])
        return url

    @property
    def edit_url(self):
        url = reverse('tracks.edit', args=[self.id])
        return url

    @property
    def delete_url(self):
        url = reverse('tracks.delete', args=[self.id])
        return url

    @property
    def image_url(self):
        return f'/media/{self.logo}'







