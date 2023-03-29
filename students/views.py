from django.shortcuts import render, HttpResponse, redirect
from students.models import Student
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.db.models import Q

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
@login_required
def list_students(request):
    # 'SELECT * FROM STUDENTS'
    # if request.user.is_authenticated:
    students = Student.objects.all()
    # students = Student.objects.filter(name__icontains="karim")
    # students = Student.objects.filter(
    #     Q(age__gte=12) | Q(course="001"), height__gt=100)
    print(students.query)
    return render(request, 'students/list_students.html', {"students": students})
    # else:
    # return redirect("/admin/login/")

# Create View


@login_required
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


# Update
def update_student(request, id):
    student = Student.objects.get(id=id)

    if request.method == 'GET':
        print(student.height)
        return render(request, 'students/update_student.html', {"student": student})
    else:
        name = request.POST.get("name")
        age = request.POST.get("age")
        height = request.POST.get("height")
        course = request.POST.get("course")
        address = request.POST.get("address")

        student.name = name
        student.age = age
        student.height = height
        student.course = course
        student.address = address

        student.save()

        return redirect(reverse_lazy("students:update", kwargs={"id": id}))

# Delete


def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect(reverse_lazy("students:list"))

# Retrive


def detail_student(request, id):
    student = Student.objects.get(id=id)
    print(student.age)
    return render(request, 'students/detail_student.html', {"student": student})


def home(request):
    return redirect(reverse_lazy("students:list"))
