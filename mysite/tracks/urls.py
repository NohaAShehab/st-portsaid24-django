
from django.urls import path, include
from tracks.views import tracks_view, tracks_home, index, show
urlpatterns = [
    path('index', tracks_view),
    path('home/',tracks_home),
    path('', index, name='tracks.index'),
    path('<int:track_id>', show, name='tracks.show')

]
