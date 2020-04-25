from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView

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