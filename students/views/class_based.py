from django.views.generic.base import View
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

from students.models import Student


class ListStudent(View):
    # "GET"
    def get(self, request):
        students = Student.objects.all()
        return render(request, 'students/list_students.html', {"students": students})

    # def post(self, request):
    #     pass


class StudentList(ListView):
    model = Student
    template_name = 'students/list_students.html'
    context_object_name = 'students'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = 34
        return context


class AddStudent(CreateView):
    model = Student
    template_name = 'about.html'
    fields = '__all__'


class UpdateStudent(UpdateView):
    model = Student
    fields = '__all__'
    template_name = 'students/update_student.html'


class StudentDetail(DetailView):
    model = Student
    template_name = 'students/detail_student.html'


class DeleteStudent(DeleteView):
    model = Student
    success_url = reverse_lazy("students:list")


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
