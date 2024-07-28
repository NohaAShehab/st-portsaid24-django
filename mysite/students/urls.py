# add all students urls to this file


from django.urls import path
from students.views import itiview
from students.views import (home, profile,
    all_students, std_profile, std_list)
urlpatterns = [
    path('iti', itiview),
    path('home', home),
    path('profile/<username>', profile),
    path('stds', all_students),
    path('stds/<int:id>',std_profile),
    path('list', std_list)
]

