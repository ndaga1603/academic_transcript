from django import forms
from .models import *



class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class ResuultForm(forms.Form):
    registration_number = forms.CharField(max_length=20)


# class ClassModuleForm(forms.ModelForm):
#     class Meta:
#         model = Class_Module
#         fields = '__all__'
