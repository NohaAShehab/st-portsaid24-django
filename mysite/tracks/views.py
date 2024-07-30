from django.shortcuts import render
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