from django.shortcuts import render, HttpResponse, redirect
from students.models import Student

# Create your views here.


def welcome(request):
    # return HttpResponse("Welcome to Django")
    name = "Amin"
    context = {"name": name, "title": "TEst 2"}
    print(request.path)

    return render(request, 'index.html', context)


def list_students(request):
    # 'SELECT * FROM STUDENTS'
    students = Student.objects.all()
    return render(request, 'students/list_students.html', {"students": students})


def home(request):
    return redirect("/students")
