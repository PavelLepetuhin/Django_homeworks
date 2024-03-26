
from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Book

def book_list(request):
    template1 = 'books/books_list.html'
    books = Book.objects.all().order_by('name')
    paginator = Paginator(books, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, template1, {'page_obj': page_obj})


def book_list_by_date(request, pub_date):
    template = 'books/books_list.html'
    books = Book.objects.filter(pub_date=pub_date)
    paginator = Paginator(books, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, template, {'page_obj': page_obj})


def book_detail(request, pub_date):
    book = Book.objects.get(pub_date=pub_date)
    books_by_date = Book.objects.filter(pub_date=book.pub_date)
    paginator = Paginator(books_by_date, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'base.html', {'book': book, 'page_obj': page_obj})
