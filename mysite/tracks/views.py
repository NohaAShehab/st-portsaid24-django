from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from tracks.models import Track
from tracks.forms import TrackForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView

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


## build all views --> using class based views ??

#### I want to use class based views to create track
from django.views import View

class TrackCreate(View):
    # get request ?
    def get(self, request, *args, **kwargs):
        # return with create form
        form = TrackForm()
        return render(request, 'tracks/create.html',
                      {'form': form})

    # post request
    def post(self, request, *args, **kwargs):
        form = TrackForm(request.POST, request.FILES)
        if form.is_valid():
            track = form.save()
            return redirect(track.show_url)





# using generic views

### using django class based views- --> generic views
#  create

class TrackCreateGeneric(CreateView):
    #form I will use to create object ?
    form_class = TrackForm
    template_name = 'tracks/creategeneric.html'
    success_url = '/tracks/'


class TrackEdit(UpdateView):
    form_class = TrackForm
    template_name = 'tracks/edit.html'
    success_url = '/tracks/'
    model = Track

#  delete
class TrackDelete(DeleteView):
    template_name = 'tracks/delete.html'
    success_url = '/tracks/'
    model = Track

# generic views list all items

class TrackDetail(DetailView):
    template_name = 'tracks/detail.html'
    model = Track
    context_object_name = 'mytrack'

class TrackListView(ListView):
    template_name = 'tracks/list.html'
    model = Track
    context_object_name = "tracks"




### when you need to use login and regisration provided by django

## class based views  --> you will use it later ---> APIs -> django rest



















