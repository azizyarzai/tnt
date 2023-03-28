
from django.urls import path
from students.views import (
    list_students,
    add_student,
    update_student,
    delete_student,
    detail_student
)

# students
# students/add
app_name = 'students'
urlpatterns = [
    path("", list_students, name='list'),
    path("add/", add_student, name='add'),
    path("update/<int:id>/", update_student, name='update'),
    path("delete/<int:id>/", delete_student, name='delete'),
    path("detail/<int:id>/", detail_student, name='detail'),
]
