from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.http import HttpResponse
# Create your views here.
from students.models import Student

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
            # return HttpResponse(std.values())
            return render(request, 'students/show.html',
                          context={"student":std})
    else:
        return HttpResponse("Student not found.")


def std_list(request):

    # send students to display in html page ?
    return render(request, 'students/list.html',
                  context={'students': students})


def landing(request):
    return HttpResponse("<h1 style='color:green'>landing</h1>")



# click std --> show its info --> redirect to page
# with the same style
# image --> show image
# after adding static folder to the project
# you must restart the server



# get all students from databases
# use models
def index(request):
    #1- get objects from database
    students = Student.objects.all()
    print(students)
    # return with templates
    return  render(request, 'students/index.html',
                   context={'students': students})


def show(request, id ):
    # get one object from db
    # student = Student.objects.get(id=id)
    student = get_object_or_404(Student, id=id)
    return render(request, 'students/showdb.html',
                  context={'student': student})


def delete(request, id):
    student = Student.objects.get(id=id)
    student.delete()  # delete object from table
    url = reverse('students.index') # covert url name to url
    return redirect(url)



def create(request):
    print(f"request here {request}")
    if request.method == 'POST':
        print(request.POST) # contains data sent with the post request
        print(f"name= {request.POST['name']}")
        print(request.FILES)
        # to create object
        std = Student()
        std.name =request.POST['name']
        std.grade = request.POST['grade']
        std.email= request.POST['email']
        std.track= request.POST['track']
        std.image = request.FILES['image']
        std.save()
        # url = reverse('students.index')  # covert url name to url
        # return redirect(url)
        return redirect(std.show_url)




        return HttpResponse("<h1 style='color:green'>Post request received </h1>")
    return render(request, 'students/create.html')




def edit(request, id):
    # get object from db ?
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        # get data , update object ??
        student.name = request.POST['name']
        pass

    return render(request, 'students/edit.html',
                  context={'student': student})















