
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
    StudentDetail,
    UpdateStudent,
    DeleteStudent
)

# students
# students/add
app_name = 'students'
urlpatterns = [
    path("", StudentList.as_view(), name='list'),
    path("add/", add_student, name='add'),
    path("update/<int:pk>/", UpdateStudent.as_view(), name='update'),
    path("delete/<int:pk>/", DeleteStudent.as_view(), name='delete'),
    path("detail/<int:pk>/", StudentDetail.as_view(), name='detail'),
]
