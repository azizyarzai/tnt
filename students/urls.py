
from django.urls import path
from students.views import list_students, add_student

# students
# students/add
urlpatterns = [
    path("", list_students),
    path("add/", add_student)
]
