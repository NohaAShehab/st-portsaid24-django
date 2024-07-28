
from django.urls import path, include
from tracks.views import tracks_view
urlpatterns = [
    path('index', tracks_view),
]
