from django import forms
from .models import Student, Address, Student2, StudentProfile, Address2
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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
        model = Student2  
        fields = ['name', 'addresses']  

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


        