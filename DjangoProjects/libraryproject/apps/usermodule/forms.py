from django import forms
from .models import Student, Address, Student2, StudentProfile, Address2



class ProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['student_name', 'profile_image']

class Student2Form(forms.ModelForm):
    class Meta:
        model = Student2
        fields = ['name', 'addresses']
        


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student2  # Make sure this says Student2
        fields = ['name', 'addresses']  # Must match the name in models.py
        