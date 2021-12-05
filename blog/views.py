from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post, Book

def index(request):
    context = {}
    index_list = Book.objects.filter(is_book_club=True)
    context = {"index_list": index_list}
    return render(request, 'blog/index.html', context)

def about(request):
    context = {}
    return render(request, 'blog/about.html', context)