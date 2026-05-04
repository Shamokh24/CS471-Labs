from django.shortcuts import render
from django.db.models import Count
from .models import Student, Student2, StudentProfile
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import StudentForm, ProfileForm, Student2Form
from django.shortcuts import render, redirect, get_object_or_404

def student_city_count(request):
    # This groups students by their address city and counts them
    city_counts = Student.objects.values('address__city').annotate(count=Count('id'))
    return render(request, 'usermodule/city_count.html', {'city_counts': city_counts})


def student_list(request):
    #students = Student.objects.all()
    #return render(request, 'usermodule/student_list.html', {'students': students})
    students = Student2.objects.all() 
    return render(request, 'usermodule/student_list.html', {'students': students})

# apps/usermodule/views.py
def student_add(request):
    # Make sure this is Student2Form!
    form = Student2Form(request.POST or None) 
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, 'usermodule/student_form.html', {'form': form})

def student_update(request, id):
    student = get_object_or_404(Student2, id=id)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, 'usermodule/student_form.html', {'form': form})

def student_delete(request, id):
    student = get_object_or_404(Student2, id=id)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'usermodule/student_delete.html', {'student': student})

def upload_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES) # FILES is required for images
        if form.is_valid():
            form.save()
            return redirect('profile_list')
    else:
        form = ProfileForm()
    return render(request, 'usermodule/upload.html', {'form': form})

def student2_add(request):
    form = Student2Form(request.POST or None)
    if form.is_valid():
        form.save() # Django handles saving the Many-to-Many links automatically
        return redirect('student_list')
    return render(request, 'usermodule/student_form.html', {'form': form})

def profile_list(request):
    profiles = StudentProfile.objects.all()
    return render(request, 'usermodule/profile_list.html', {'profiles': profiles})