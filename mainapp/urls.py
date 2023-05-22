from django.urls import path
from .views import SchoolListView, SchoolCreateView, SchoolUpdateView, SchoolDeleteView, \
    StudentListView, StudentCreateView, StudentUpdateView, StudentDetailAPIVIEW, SchoolDetailAPIVIEW, SchoolAPIView, \
    SchoolDetailAPIView, StudentAPIView, StudentDetailAPIView

app_name = 'mainapp'

urlpatterns = [
    path('schools/', SchoolListView.as_view(), name='school_list'),
    path('schools/create/', SchoolCreateView.as_view(), name='school_create'),
    path('schools/<int:school_id>/update/', SchoolUpdateView.as_view(), name='school_update'),
    path('schools/<int:school_id>/delete/', SchoolDeleteView.as_view(), name='school_delete'),
    path('students/', StudentListView.as_view(), name='student_list'),
    path('students/create/', StudentCreateView.as_view(), name='student_create'),
    path('students/<int:student_id>/update/', StudentUpdateView.as_view(), name='student_update'),
    path('api/studentdetailsapi/', StudentDetailAPIVIEW.as_view(), name='student retrieve api'),
    path('api/schooldetailsapi/', SchoolDetailAPIVIEW.as_view(), name='school retrieve api'),
    path('api/schools/', SchoolAPIView.as_view(), name='school_api_list'),
    path('api/schools/<int:school_id>/', SchoolDetailAPIView.as_view(), name='school_api_detail'),
    path('api/students/', StudentAPIView.as_view(), name='student_api_list'),
    path('api/students/<int:student_id>/', StudentDetailAPIView.as_view(), name='student')
]
