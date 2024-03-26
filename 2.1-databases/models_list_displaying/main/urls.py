"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import utils
from books.views import book_list, book_list_by_date, book_detail

urlpatterns = [
    path('', book_list, name='books'),
    path('posts/<pub_date>/', book_list_by_date, name='book_list_by_date'),
    path('book/<pub_date>/', book_detail, name='book_detail'),
    path('admin/', admin.site.urls),
]

# path('posts/<date:pud_date>/', book_list_by_date, name='book_list_by_date'),