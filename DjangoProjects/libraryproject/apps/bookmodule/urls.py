from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('index2/<int:val1>/', views.index2),
    path('<int:bookId>', views.viewbook),
    path('', views.index, name= "books.index"),
    path('list_books/', views.list_books, name= "books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path('html5/links/', views.links_page, name='books.links'),
    path('html5/text/formatting/', views.text_formatting_page, name='books.text_formatting'),
    path('html5/listing/', views.listing_page, name='books.listing'),
    path('html5/tables/', views.tables_page, name='books.tables'),
    path('search/', views.filterbooks, name='books.search'),
    path('simple/query/', views.simple_query, name='books.simple_query'),
    path('complex/query/', views.complex_query, name='books.complex_query'),
    path('lab8/task1/', views.task1, name='lab8.task1'),
    path('lab8/task2/', views.task2, name='lab8.task2'),
    path('lab8/task3/', views.task3, name='lab8.task3'),
    path('lab8/task4/', views.task4, name='lab8.task4'),
    path('lab8/task5/', views.task5, name='lab8.task5'),
    path('lab9/all/', views.lab9_all_tasks, name='lab9_all'),

]
