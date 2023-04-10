from rest_framework import serializers
from students.models import Student


# class StudentSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=10)
#     age = serializers.IntegerField()

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        # fields = '__all__'
        exclude = ['user']
