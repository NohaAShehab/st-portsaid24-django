
from django.urls import path, include
from tracks.views import tracks_view, tracks_home
urlpatterns = [
    path('index', tracks_view),
    path('home/',tracks_home),
]
