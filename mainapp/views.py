from django.shortcuts import render
from rest_framework import generics, status
from django.views import View
from .models import Student, School
from .serializers import SchoolSerializer, StudentSerializer
from rest_framework.response import Response
from .forms import StudentForm, SchoolForm
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
class SchoolListView(View):
    def get(self, request):
        schools = School.objects.all()
        return render(request, 'mainapp/school_list.html')
    
class SchoolCreateView(View):
    def get(self, request):
        form = SchoolForm()
        data = {}
        return render(request, 'mainapp/school_form.html')
    def post(self, request):
        form = SchoolForm(request.POST)
        if form.is_valid():
            school = form.save()
            data = {'success':True, 'message' : 'School created successfully'}
        else:
            data = {'success':False, 'message' : 'Invalid data'}
class SchoolUpdateView(View):
    def get(self, request, school_id):
        school = get_object_or_404(School, id=school_id)
        form = SchoolForm(instance=school)
        data = {}
        return render(request, 'mainapp/school_form.html')
    def post(self, request, school_id):
        school = get_object_or_404(School, id=school_id)
        form = SchoolForm(request.POST, instance=school)
        if form.is_valid():
            school = form.save()
            data = {'success':True, 'message' : 'School updated successfully'}
        else:
            data = {'success':False, 'message' : 'Invalid data'}
        return render(request, 'mainapp/school_form.html', {'form':form, 'data':data})
    
class SchoolDeleteView(View):
    def post(self, request, school_id):
        school = get_object_or_404(School, id=school_id)
        school.delete()
        data = {'success': True, 'message' : 'school deleted successfully'}

class StudentListView(View):
    def get(self, request):
        students =Student.objects.all()
        return render(request, 'mainapp/student_list.html', {'students':students})
class StudentCreateView(View):
    def get(self, request):
        form = StudentForm()
        data = {}
        return render(request, 'mainapp/student_form.html', {'form':form, 'data':data})
    def post(self, request):
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            data = {'success': True, 'message' : 'student created successfully'}
        else:
            data = {'success':False, 'message' : 'Invalid data'}
        return render(request, 'mainapp/student_form.html', {'form':form, 'data':data})

class StudentUpdateView(View):
    def get(self, request, student_id):
        student = get_object_or_404(Student, id=student_id)
        form = StudentForm(instance=student)
        data = {}
        return render(request, 'mainapp/static/student_form.html', {'form':form, 'data':data})
    def post(self, request, student_id):
        student = get_object_or_404(Student, id=student_id)
        form = StudentForm(instance=student)
        if form.is_valid():
            form.save()
            data =  {'success': True, 'message' : 'student updated successfully'}


class SchoolAPIView(APIView):
    def get(self, request):
        schools = School.objects.all()
        serializer = SchoolSerializer(schools, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SchoolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True, 'message': 'School created successfully.'})
        return Response({'success': False, 'message': 'Invalid data.'})

class SchoolDetailAPIView(APIView):
    def get_object(self, school_id):
        return get_object_or_404(School, id=school_id)

    def get(self, request, school_id):
        school = self.get_object(school_id)
        serializer = SchoolSerializer(school)
        return Response(serializer.data)

    def put(self, request, school_id):
        school = self.get_object(school_id)
        serializer = SchoolSerializer(school, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True, 'message': 'School updated successfully.'})
        return Response({'success': False, 'message': 'Invalid data.'})

    def delete(self, request, school_id):
        school = self.get_object(school_id)
        school.delete()
        return Response({'success': True, 'message': 'School deleted successfully.'})

class StudentAPIView(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True, 'message': 'Student created successfully.'})
        return Response({'success': False, 'message': 'Invalid data.'})

class StudentDetailAPIView(APIView):
    def get_object(self, student_id):
        return get_object_or_404(Student, id=student_id)

    def get(self, request, student_id):
        student = self.get_object(student_id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self, request, student_id):
        student = self.get_object(student_id)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True, 'message': 'Student updated successfully.'})
        return Response({'success': False, 'message': 'Invalid data.'})

    def delete(self, request, student_id):
        student = self.get_object(student_id)
        student.delete()
        return Response({'success': True, 'message': 'Student deleted successfully.'})
    
class SchoolDetailAPIVIEW(generics.RetrieveAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        response_data = {
            'status': True,
            'message': 'School details retrieve',
            'data' : serializer.data
        }
        return Response(response_data)

class StudentDetailAPIVIEW(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        response_data = {
            'status': True,
            'message': 'School details retrieve',
            'data' : serializer.data
        }
        return Response(response_data)