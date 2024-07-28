# add all students urls to this file


from django.urls import path
from students.views import itiview
from students.views import home
urlpatterns = [
    path('iti', itiview),
    path('home', home),
]
