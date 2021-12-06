from typing import Text
from django.db import models
from django.conf import settings
from django.utils.timezone import now

class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    cover_url = models.URLField(max_length=200, null=True)
    is_book_club = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} ({self.author})'

class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=2500)
    rating = models.IntegerField(default=0)
    date = models.DateTimeField(default=now, editable=False)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} ({self.date}) "{self.text} {self.rating}" - {self.book}'

class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    date = models.DateTimeField(default=now, editable=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'"{self.text}" - {self.author}'