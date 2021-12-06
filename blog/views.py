from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post, Book, Comment, Category
from .forms import PostForm, BookForm, CommentForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

def index(request):
    context = {}
    index_list = Book.objects.filter(is_book_club=True)
    context = {"index_list": index_list}
    return render(request, 'blog/index.html', context)

def about(request):
    context = {}
    return render(request, 'blog/about.html', context)

class PostListView(generic.ListView):
    model = Post
    template_name = 'blog/posts.html'

class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/detail_post.html'

class BookListView(generic.ListView):
    model = Book
    template_name = 'blog/books.html'
    queryset = Book.objects.order_by('name')

class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'blog/detail_book.html'

class CategoryListView(generic.ListView):
    model = Category
    template_name = 'blog/categories.html'

def category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    context = {}
    post_set = Post.objects.filter(category=category_id)
    context = {"post_set": post_set, "category": category}
    return render(request, 'blog/category.html', context)

class PostCreateView(LoginRequiredMixin, PermissionRequiredMixin, generic.edit.CreateView):
    model = Post
    template_name = 'blog/create_post.html'
    fields = [
            'title',
            'text',
            'rating',
            'book',
        ]
    success_url = reverse_lazy('blog:posts')
    permission_required = 'blog.add_post'

@login_required
@permission_required('blog.add_book')
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

class PostUpdateView(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    model = Post
    fields = [
            'title',
            'text',
            'rating',
            'book',
        ]
    template_name = 'blog/update.html'
    permission_required = 'blog.change_post'

class PostDeleteView(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    model = Post
    template_name = 'blog/delete.html'
    success_url = reverse_lazy('blog:posts')
    permission_required = 'blog.delete_post'

@login_required
def create_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_author = request.user
            comment_text = form.cleaned_data['text']
            comment = Comment(author=comment_author,
                            text=comment_text,
                            post=post)
            comment.save()
            return HttpResponseRedirect(
                reverse('blog:detail_post', args=(post_id, )))
    else:
        form = CommentForm()
    context = {'form': form, 'post': post}
    return render(request, 'blog/create_comment.html', context)
