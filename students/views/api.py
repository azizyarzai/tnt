from students.serializers import StudentSerializer
from django.http import JsonResponse
from students.models import Student
from rest_framework.response import Response
from rest_framework.decorators import api_view, APIView
from rest_framework import status


@api_view(['GET', 'POST'])
def test(request):
    # JSON -> Python object
    serializer = StudentSerializer(data=request.data)

    if serializer.is_valid():
        return Response(serializer.validated_data)
    else:
        return Response(serializer.errors)


class ListStudentAPiView(APIView):
    def get(self, request):
        students = Student.objects.filter(name__icontains='ahmad')
        # Queryset -> JSON
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            res = serializer.save()

            ser = StudentSerializer(res)
            return Response(ser.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
