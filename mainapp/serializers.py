from rest_framework import serializers
from .models import Student, School
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class SchoolSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True, read_only = True)

    class Meta:
        model = School
        fields = '__all__'
        read_only_fields = ['students']