from django.forms import ModelForm
from .models import Book, Post, Comment


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = [
            'name',
            'author',
            'cover_url',
            'is_book_club',
        ]
        labels = {
            'name': 'Título',
            'author': 'Autor',
            'cover_url': 'URL da Capa',
            'is_book_club': 'Clube do Livro',
        }


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'text',
            'rating',
            'book',
        ]
        labels = {
            'title': 'Título',
            'text': 'Resenha',
            'rating': 'Nota',
            'book': 'Livro',
        }

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = [
            'text',
        ]
        labels = {
            'text': 'Comentário',
        }