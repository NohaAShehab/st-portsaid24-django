from django.db import models

# Create your models here.

# create new model => descript students
# id ,name, track, image, email, grade

class Student(models.Model):
    # django models ->provides ? datatypes you can use while definning
    # the columns
    # null property works on db level, blank works on admin dashboard level
    name =models.CharField(max_length=100)
    image= models.CharField(max_length=100, null=True)
    track = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True, unique=True)
    grade = models.IntegerField(default=0, null=True, blank=True)


    def __str__(self):
        return self.name


