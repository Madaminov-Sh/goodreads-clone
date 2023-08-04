from django.contrib import admin

from .models import Book, BookAuthor, BookReview


class BooksAdmin(admin.ModelAdmin):
    list_display = ['title','description', 'isbn']

admin.site.register(Book, BooksAdmin)

