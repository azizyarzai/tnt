
from django.urls import path
from students.views import list_students, add_student, update_student

# students
# students/add
urlpatterns = [
    path("", list_students),
    path("add/", add_student),
    path("update/<int:id>/", update_student)
]
