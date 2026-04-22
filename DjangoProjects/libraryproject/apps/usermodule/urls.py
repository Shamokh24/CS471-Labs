from . import views
from django.urls import path
urlpatterns = [
    path('city_count/', views.city_count, name='students.city_count'),
]