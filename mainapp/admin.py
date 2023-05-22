from django.contrib import admin
from .models import School, Student
# Register your models here.
@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'create_at',  'update_at')
    search_fields = ['name']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'enrollment', 'school', 'create_at',  'update_at')
    search_fields = ['name', 'enrollment', 'school_name']