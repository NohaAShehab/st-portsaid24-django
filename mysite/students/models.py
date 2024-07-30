from django.db import models
from django.shortcuts import reverse


class Student(models.Model):

    name =models.CharField(max_length=100)
    # image= models.CharField(max_length=100, null=True)
    track = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True, unique=True)
    grade = models.IntegerField(default=0, null=True, blank=True)
    # upload images
    image = models.ImageField(upload_to='students/images',
                              null=True, blank=True)


    def __str__(self):
        return self.name

    @property
    def image_url(self):
        return f'/media/{self.image}'

    @property
    def show_url(self):
        url = reverse('students.show', args=[self.id])
        return url

    @property
    def edit_url(self):
        url = reverse('students.edit', args=[self.id])
        return url




