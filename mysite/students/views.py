from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.http import HttpResponse
# Create your views here.
from students.models import Student
from tracks.models import Track
from students.forms import StudentForm, StudentModelForm

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
    tracks= Track.objects.all()
    if request.method == 'POST':

        # validate data ??
        # check if name not empty string
        # check if email ?? not exists in db ??
        ## check if image is valid image

        print(request.POST) # contains data sent with the post request
        print(f"name= {request.POST['name']}")
        print(request.FILES)
        # to create object
        std = Student()
        std.name =request.POST['name']

        if request.POST['grade'] !='':
            std.grade = request.POST['grade']

        std.email= request.POST['email']
        if 'track' in request.POST:
            track = Track.objects.filter(id=request.POST['track']).first() # return queryset
            if(track):
                std.track=track

        if 'image' in request.FILES:
            std.image = request.FILES['image']
        std.save()
        # url = reverse('students.index')  # covert url name to url
        # return redirect(url)
        return redirect(std.show_url)

    return render(request, 'students/create.html',
                context={"tracks":tracks}  )




# def edit(request, id):
#     # get object from db ?
#     student = get_object_or_404(Student, id=id)
#     if request.method == 'POST':
#         # get data , update object ??
#         student.name = request.POST['name']
#         pass
#
#     return render(request, 'students/edit.html',
#                   context={'student': student})






def create_via_form(request):
    myform= StudentForm()
    if request.method == 'POST':
        print(request.POST, request.FILES)
        # form ---> apply is valid ??
        myform = StudentForm(request.POST, request.FILES)
        if myform.is_valid():
            student= Student.objects.create(name=myform.cleaned_data['name'],
            email=myform.cleaned_data['email'],grade=myform.cleaned_data['grade']
                                            ,image=myform.cleaned_data['image'],
                                            track= myform.cleaned_data['track'])
            student.save()
            return redirect(student.show_url)


    return  render(request, 'students/forms/create.html',
                   context={'form':myform})



def create_via_model_form(request):
    form  =StudentModelForm()
    if request.method=='POST':
        form = StudentModelForm(request.POST, request.FILES)
        if form.is_valid():
            # create new object
            student = form.save()
            return redirect(student.show_url)

    return render(request, 'students/forms/createmodel.html',
                  context={'form':form})




def edit(request, id):
    student = get_object_or_404(Student, id=id)
    form = StudentModelForm(instance=student) #populate form with student data
    if request.method == 'POST':
        form = StudentModelForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect(student.show_url)

    return render(request, 'students/forms/edit.html',
                  context={ 'form':form})


