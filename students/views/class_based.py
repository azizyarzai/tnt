from django.views.generic.base import View
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView

from students.models import Student


class ListStudent(View):
    # "GET"
    def get(self, request):
        students = Student.objects.all()
        return render(request, 'students/list_students.html', {"students": students})

    # def post(self, request):
    #     pass


class CreateStudent(View):
    # "GET"
    def get(self, request):
        return render(request, 'students/add_student.html')

    def post(self, request):
        name = request.POST.get("name")
        height = request.POST.get("height")
        course = request.POST.get("course")
        address = request.POST.get("address")

        # image = request.FILES.get("image")

        Student.objects.create(
            name=name, height=height, course=course, address=address)

        return redirect("/")


class AddStudent(CreateView):
    model = Student
    fields = '__all__'
    template_name = 'about.html'
