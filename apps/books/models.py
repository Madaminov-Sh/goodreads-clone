from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    isbn = models.CharField(max_length=17)

    def __str__(self):
        return self.title


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    bio = models.TextField()

    def __str__(self):
        return self.email


class BookAuthor(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author} | P{self.book}"


class BookReview(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    stars_review = models.IntegerField(validators=[
        MinValueValidator(1), MaxValueValidator(5)
    ])

    def __str__(self):
        return self.book
