from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# functions
# handle http request?
# system --> students and courses and tracks

def itiview(request):
    print(request)
    #
    return HttpResponse("<h1 style='color:red'>iti</h1>")

def home(request):
    return HttpResponse("<h1 style='color:green'>Home</h1>")