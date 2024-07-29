from django.contrib import admin


# each app you have ==> contains file admin ??
# you can add your models here
# Register your models here.
from students.models import Student
admin.site.register(Student)
