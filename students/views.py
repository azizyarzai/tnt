from django.shortcuts import render, HttpResponse, redirect
from students.models import Student

# Create your views here.


def welcome(request):
    # return HttpResponse("Welcome to Django")
    name = "Amin"
    context = {"name": name, "title": "TEst 2"}
    print(request.path)

    return render(request, 'index.html', context)


# CRUD (Create, Read, Update, Delete)
# Read
# List View
def list_students(request):
    # 'SELECT * FROM STUDENTS'
    students = Student.objects.all()
    return render(request, 'students/list_students.html', {"students": students})

# Create View


def add_student(request):
    print(dir(request))
    if request.method == 'GET':
        return render(request, 'students/add_student.html')
    else:
        name = request.POST.get("name")
        age = request.POST.get("age")
        height = request.POST.get("height")
        course = request.POST.get("course")
        address = request.POST.get("address")

        Student.objects.create(
            name=name, age=age, height=height, course=course, address=address)

        return redirect("/")


def home(request):
    return redirect("/students")
