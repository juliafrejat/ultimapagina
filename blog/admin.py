from django.contrib import admin
from .models import Book, Category, Post, Comment

admin.site.register(Book)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)