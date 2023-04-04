
from django.urls import path
from students.views.func_based import (
    list_students,
    add_student,
    update_student,
    delete_student,
    detail_student
)
from students.views.class_based import (
    ListStudent,
    CreateStudent,
    StudentList,
    StudentDetail
)

# students
# students/add
app_name = 'students'
urlpatterns = [
    path("", StudentList.as_view(), name='list'),
    path("add/", CreateStudent.as_view(), name='add'),
    path("update/<int:id>/", update_student, name='update'),
    path("delete/<int:id>/", delete_student, name='delete'),
    path("detail/<int:pk>/", StudentDetail.as_view(), name='detail'),
]
