from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.db.models import Q , F
from django.db.models import Count, Sum, Avg, Max, Min
from django.db.models.functions import Coalesce

def task1(request):
    books = Book.objects.filter(Q(price__lte=80))
    return render(request, 'bookmodule/bookList.html', {'books': books})

def task2(request):
    books = Book.objects.filter(Q(edition__gt=3) & (Q(author__contains='qu') | Q(title__icontains='qu')))
    return render(request, 'bookmodule/bookList.html', {'books': books})

def task3(request):
    books = Book.objects.filter(Q(edition__lte=3) & ~(Q(author__contains='qu') | Q(title__icontains='qu')))
    return render(request, 'bookmodule/bookList.html', {'books': books})

def task4(request):
    books = Book.objects.order_by('title')
    return render(request, 'bookmodule/bookList.html', {'books': books})

def task5(request):
    stats = Book.objects.aggregate(
        total_books=Count('id'),
        total_price=Sum('price'),
        average_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )
    return render(request, 'bookmodule/bookList.html', {'stats': stats})


def index(request):
        name = request.GET.get("name") or "world!"
        return render(request, "bookmodule/index.html" , {"name": name})  #your render line
    
def index2(request, val1 = 0):   #add the view function (index2)
        return HttpResponse("value1 = "+str(val1))
def viewbook(request, bookId):
        # assume that we have the following books somewhere (e.g. database)
        book1 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'}
        book2 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam'}
        targetBook = None
        if book1['id'] == bookId: targetBook = book1
        if book2['id'] == bookId: targetBook = book2
        context = {'book':targetBook} # book is the variable name accessible by the template
        return render(request, 'bookmodule/show.html', context)
def index(request):
        return render(request, "bookmodule/index.html")
    
def list_books(request):
        return render(request, 'bookmodule/list_books.html')
    
def viewbook(request, bookId):
        return render(request, 'bookmodule/one_book.html')
    
def aboutus(request):
        return render(request, 'bookmodule/aboutus.html')

def links_page(request):
        return render(request, 'bookmodule/links.html')

def text_formatting_page(request):
        return render(request, 'bookmodule/text_formatting.html')

def listing_page(request):
        return render(request, 'bookmodule/listing.html')
        
def tables_page(request):
    return render(request, 'bookmodule/tables.html')

def __getBooksList():
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
    book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
    book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
    return [book1, book2, book3]

def filterbooks(request):
       if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')
        # now filter
        books = __getBooksList()
        newBooks = []
        for item in books:
            contained = False
            if isTitle and string in item['title'].lower(): contained = True
            if not contained and isAuthor and string in item['author'].lower():contained = True
            
            if contained: newBooks.append(item)
        return render(request, 'bookmodule/bookList.html', {'books':newBooks})

def simple_query(request):
    mybooks=Book.objects.filter(title__icontains='and') # <- multiple objects
    return render(request, 'bookmodule/bookList.html', {'books':mybooks})

def complex_query(request):
    mybooks=books=Book.objects.filter(author__isnull = False)[:10]#.filter(title__icontains='and').filter(edition__gte = 2).exclude(price__lte = 100)[:10]
    if len(mybooks)>=1:
        return render(request, 'bookmodule/bookList.html', {'books':mybooks})
    else:
        return render(request, 'bookmodule/index.html')


def lab9_all_tasks(request):
    # --- Task 1: Percentage (Calculated in View for performance) ---
    total_qty = NBook.objects.aggregate(t=Sum('quantity'))['t'] or 1
    books = NBook.objects.annotate(
        percentage=(F('quantity') * 100.0) / total_qty
    )

    # --- Tasks 2, 4, 5, 6: Publisher Annotations ---
    publishers = Publisher.objects.annotate(
        total_stock=Coalesce(Sum('nbook__quantity'), 0),
        avg_price=Coalesce(Avg('nbook__price'), 0.0),
        min_price=Coalesce(Min('nbook__price'), 0.0),
        max_price=Coalesce(Max('nbook__price'), 0.0),
        # Task 5: High Rating (e.g., rating >= 4)
        highly_rated=Count('nbook', filter=Q(nbook__rating__gte=3)),
        # Task 6: Custom Filter
        task6_count=Count('nbook', filter=Q(
            nbook__price__gt=50, 
            nbook__quantity__lt=5, 
            nbook__quantity__gte=1
        ))
    )

    # --- Task 3: Oldest Books ---
    old_dates = Publisher.objects.annotate(
        old_d=Min('nbook__pubdate')
    ).values_list('old_d', flat=True)
    
    oldest_books = NBook.objects.filter(pubdate__in=old_dates)

    context = {
        'books': books,
        'publishers': publishers,
        'oldest_books': oldest_books
    }

    return render(request, 'bookmodule/lab9.html', context)