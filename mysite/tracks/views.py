from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def tracks_view(request):
    return HttpResponse("<h1 style='color:red; text-align:center'>Tracks Home </h1>")


def tracks_home(request):
    return render(request, 'tracks/list.html')