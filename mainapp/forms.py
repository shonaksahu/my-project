from django import forms
from .models import School, Student

class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = '__all__'
        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'create_at' : forms.DateInput(attrs={'class' : 'form-control'}),
            'update_at' : forms.DateInput(attrs={'class' : 'form-control'}),
        }

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'enrollment' : forms.TextInput(attrs={'class' : 'form-control'}),
            'school' : forms.TextInput(attrs={'class' : 'form-control'}),
            'create_at' : forms.DateInput(attrs={'class' : 'form-control'}),
            'update_at' : forms.DateInput(attrs={'class' : 'form-control'}),
        }