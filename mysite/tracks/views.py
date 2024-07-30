from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from tracks.models import Track
# Create your views here.

def tracks_view(request):
    return HttpResponse("<h1 style='color:red; text-align:center'>Tracks Home </h1>")


def tracks_home(request):
    return render(request, 'tracks/list.html')


def index(request):
    tracks = Track.objects.all()
    return render(request, 'tracks/index.html',
                  context={'tracks': tracks})


def show(request, track_id):
    track = get_object_or_404(Track, pk=track_id)
    return render(request, 'tracks/show.html',
                  context={'track': track})
