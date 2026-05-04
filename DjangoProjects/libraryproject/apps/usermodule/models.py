from django.db import models
from django import forms

class Address(models.Model):
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.city

class Card(models.Model):
    card_number = models.IntegerField(unique=True)

    def __str__(self):
        return str(self.card_number)

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=100)
    code = models.IntegerField(unique=True)

    def __str__(self):
        return f"{self.title} ({self.code})"

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)  
    card = models.OneToOneField(
        Card,
        on_delete=models.PROTECT,  
        related_name='student',
        null=True,
        blank=True
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE, 
        related_name='students',
        null=True,
        blank=True
    )
    courses = models.ManyToManyField(
        Course,
        related_name='students',
        blank=True
    )

    def __str__(self):
        return self.name

class StudentProfile(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='student_pics/') # Needs Pillow installed

    def __str__(self):
        return f"Profile of {self.student.name}"
    
class Address2(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name  # This tells the form what text to display

class Student2(models.Model):
    name = models.CharField(max_length=100)
    # Change this to CharField to store your "array" as a comma-separated string
    addresses = models.CharField(max_length=500, blank=True, null=True)

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student2
        fields = ['name', 'addresses']

    def clean_addresses(self):
        data = self.cleaned_data['addresses']
        if isinstance(data, str):
            return [item.strip() for item in data.split(',')]
        return data 
       
class StudentProfile(models.Model):
    student_name = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='profiles/')