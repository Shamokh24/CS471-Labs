from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('city_count/', views.student_city_count, name='students.city_count'),
    path('lab11/students/', views.student_list, name='student_list'),
    path('lab11/students/add/', views.student_add, name='student_add'),
    path('lab11/students/update/<int:id>/', views.student_update, name='student_update'),
    path('lab11/students/delete/<int:id>/', views.student_delete, name='student_delete'),
    path('lab11/upload/', views.upload_profile, name='upload_profile'),
    path('profiles/', views.profile_list, name='profile_list'), 
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)