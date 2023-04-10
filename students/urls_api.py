from django.urls import path
from students.views.api import test, ListStudentAPiView

urlpatterns = [
    path("test/", test),
    path("", ListStudentAPiView.as_view()),
]
