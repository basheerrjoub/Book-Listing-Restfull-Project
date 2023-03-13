from django.shortcuts import render
from django.views.generic import ListView
from .models import Book


class BookListView(ListView):
    """Customize the view of the list of Books added"""

    model = Book
    template_name = "book_list.html"
