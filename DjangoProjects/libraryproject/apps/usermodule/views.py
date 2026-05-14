from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from .models import Student, Student2, StudentProfile
from .forms import StudentForm, ProfileForm, Student2Form
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# --- Authentication & Registration ---

def register_view(request):
    """Handles new user registration using Django's built-in UserCreationForm."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now login.')
            return redirect('login')  # Ensure 'login' is named in your urls.py
    else:
        form = UserCreationForm()
    return render(request, 'usermodule/register.html', {'form': form})

def login_view(request):
    """Handles user login and redirects to the student list upon success."""
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.info(request, f'Login successful! Welcome, {user.username}.')
            # Redirecting to 'student_list' instead of a hardcoded path to prevent errors
            return redirect('student_list') 
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'usermodule/login.html', {'form': form})

def logout_view(request):
    """Logs out the user and redirects back to the login page."""
    logout(request)
    messages.info(request, "You have logged out.")
    return redirect('login')

# --- Student Management ---

@login_required
def student_list(request):
    """Displays all students. Requires the user to be logged in."""
    students = Student2.objects.all() 
    return render(request, 'usermodule/student_list.html', {'students': students})

def student_add(request):
    """Adds a new student using Student2Form."""
    form = Student2Form(request.POST or None) 
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, 'usermodule/student_form.html', {'form': form})

def student_update(request, id):
    """Updates an existing student's details."""
    student = get_object_or_404(Student2, id=id)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, 'usermodule/student_form.html', {'form': form})

def student_delete(request, id):
    """Deletes a student record after POST confirmation."""
    student = get_object_or_404(Student2, id=id)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'usermodule/student_delete.html', {'student': student})

# --- Profile & Media Handling ---

def upload_profile(request):
    """Handles image uploads for student profiles."""
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile_list')
    else:
        form = ProfileForm()
    return render(request, 'usermodule/upload.html', {'form': form})

def profile_list(request):
    """Displays all uploaded student profiles."""
    profiles = StudentProfile.objects.all()
    return render(request, 'usermodule/profile_list.html', {'profiles': profiles})

# --- Analytics ---

def student_city_count(request):
    """Groups students by city and provides a count for each."""
    city_counts = Student.objects.values('address__city').annotate(count=Count('id'))
    return render(request, 'usermodule/city_count.html', {'city_counts': city_counts})