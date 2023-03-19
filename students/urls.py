
from django.urls import path
from students.views import list_students

# students
# students/add
urlpatterns = [
    path("", list_students),
    path("add/", list_students)
]
