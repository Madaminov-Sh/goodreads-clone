from django.contrib import admin

from .models import Book, BookAuthor, BookReview, Author


class BooksAdmin(admin.ModelAdmin):
    list_display = ['title', 'id',  'isbn']

admin.site.register(Book, BooksAdmin)
admin.site.register(BookAuthor)
admin.site.register(Author)

