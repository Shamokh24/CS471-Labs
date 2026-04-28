from django.shortcuts import render
from .models import Student, Address, Department, Course
from django.db.models import Count, Min

# Existing views (DO NOT REMOVE)
def city_count(request):
    city_stats = Address.objects.annotate(student_count=Count('student'))
    return render(request, 'usermodule/city_count.html', {'city_stats': city_stats})

# New views for Lab 9
def department_student_count(request):
    departments = Department.objects.annotate(student_count=Count('students'))
    return render(request, 'usermodule/department_count.html', {'departments': departments})

def course_student_count(request):
    courses = Course.objects.annotate(student_count=Count('students'))
    return render(request, 'usermodule/course_count.html', {'courses': courses})

def oldest_student_per_department(request):
    departments = Department.objects.annotate(
        oldest_student_id=Min('students__id')
    ).prefetch_related('students')
    
    dept_data = []
    for dept in departments:
        oldest_student = dept.students.filter(id=dept.oldest_student_id).first()
        dept_data.append({
            'department': dept,
            'oldest_student': oldest_student
        })
    
    return render(request, 'usermodule/oldest_student.html', {'dept_data': dept_data})

def departments_more_than_two_students(request):
    departments = Department.objects.annotate(
        student_count=Count('students')
    ).filter(
        student_count__gt=2
    ).order_by('-student_count')
    
    return render(request, 'usermodule/departments_more_than_two.html', {'departments': departments})

