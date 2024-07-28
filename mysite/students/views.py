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



def profile(request,username):
    return HttpResponse(f"<h1 style='color:green'>Profile {username}</h1>")



students = [
    {'id':10, 'name':'abc', 'track':'python', 'image':'pic1.png'},
    {'id':21, 'name':'test', 'track':'python', 'image':'pic2.png'},
    {'id':33, 'name':'mmm', 'track':'python', 'image':'pic3.png'},
    {'id':4, 'name':'sss', 'track':'python', 'image':'pic4.png'}
    ]

def all_students(request):
    return HttpResponse(students)


def std_profile(request, id):
    print(type(id))
    for std in students:
        if std['id'] == id :
            return HttpResponse(std.values())
    else:
        return HttpResponse("Student not found.")


def std_list(request):

    # send students to display in html page ?
    return render(request, 'students/list.html',
                  context={'students': students})


def landing(request):
    return HttpResponse("<h1 style='color:green'>landing</h1>")