from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import Q

from .models import Book

# Create your views here.

class BookListView(LoginRequiredMixin, ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/book_list.html'
    # Redirects the user to the login page if they're not logged in
    login_url = 'account_login'

class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_detail.html'
    # Redirects the user to the login page if they're not logged in
    login_url = 'account_login'
    permission_required = 'books.special_status'

class SearchResultsListView(ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/search_results.html'
    # Search filter: case insensitive
    # queryset = Book.objects.filter(title__icontains='test')

    # Overriding the queryset method to only show objects that
    # the user search for in a get request
    def get_queryset(self):
        query = self.request.GET.get('q')
        return Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )