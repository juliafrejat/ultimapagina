from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post, Book
from .forms import PostForm, BookForm

def index(request):
    context = {}
    index_list = Book.objects.filter(is_book_club=True)
    context = {"index_list": index_list}
    return render(request, 'blog/index.html', context)

def about(request):
    context = {}
    return render(request, 'blog/about.html', context)

def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = Book(**form.cleaned_data)
            book.save()
            return HttpResponseRedirect(
                reverse('blog:detail_book', args=(book.pk, )))
    else:
        form = BookForm()
    context = {'form': form}
    return render(request, 'blog/create_book.html', context)