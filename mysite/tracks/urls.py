
from django.urls import path, include
from tracks.views import (tracks_view, tracks_home, index, show,
                          TrackCreate, TrackCreateGeneric, TrackEdit, TrackDelete,
                          TrackDetail, TrackListView)
urlpatterns = [
    path('index', tracks_view),
    path('home/',tracks_home),
    path('', index, name='tracks.index'),
    path('<int:track_id>', show, name='tracks.show'),
    path('create', TrackCreate.as_view(), name='tracks.create'),
    path('create_generic', TrackCreateGeneric.as_view(), name='tracks.create_generic'),
    path('<int:pk>/edit', TrackEdit.as_view(), name='tracks.edit'),
    path('<int:pk>/delete', TrackDelete.as_view(), name='tracks.delete'),
    path('<int:pk>/detail', TrackDetail.as_view(), name='tracks.detail'),
    path('list', TrackListView.as_view(), name='tracks.list'),

]
