from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('books/create/', views.create_book, name='create_book'),
    path('posts/', views.PostListView.as_view(), name='posts'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('categories/', views.CategoryListView.as_view(), name='categories'),
    path('categories/<int:category_id>/', views.category, name='category'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='detail_post'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='detail_book'),
    path('posts/create/', views.PostCreateView.as_view(), name='create_post'),
    path('posts/update/<int:pk>/', views.PostUpdateView.as_view(), name='update'),
    path('posts/delete/<int:pk>/', views.PostDeleteView.as_view(), name='delete'),
    path('posts/<int:post_id>/comment/', views.create_comment, name='create_comment'),
]