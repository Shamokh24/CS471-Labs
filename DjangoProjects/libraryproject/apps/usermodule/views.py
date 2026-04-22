from urllib import request

from django.shortcuts import render
from .models import Student, Address
from django.db.models import Count

def city_count(request):
    city_stats = Address.objects.annotate(student_count=Count('student'))
    context = {'city_stats': city_stats}
    return render(request, 'usermodule/city_count.html', context)
