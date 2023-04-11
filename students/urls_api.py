from django.urls import path, include
from students.views.api import test, ListStudentAPiView, StudentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("viewset", StudentViewSet)

urlpatterns = [
    path("test/", test),
    path("", ListStudentAPiView.as_view()),
    # api/students/viewset/
    # api/students/viewset/<id>
    path("", include(router.urls)),
]
