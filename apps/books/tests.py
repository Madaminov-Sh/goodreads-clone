from django.test import TestCase
from django.urls import reverse

from .models import Book


class BookTestCase(TestCase):
    def test_no_book(self):
        response = self.client.get(reverse('books:books'))
        self.assertContains(response, 'No books found')

    def test_book_list(self):
        Book.objects.create(title='book', description='desc', isbn='323232')
        Book.objects.create(title='book1', description='desc', isbn='555656')
        Book.objects.create(title='book2', description='desc', isbn='4484845')
        Book.objects.create(title='book3', description='desc', isbn='454518')

        response = self.client.get(reverse('books:books'))

        books = Book.objects.all()

        for book in books:
            self.assertContains(response, book.title)

    def test_book_detail(self):
        book = Book.objects.create(title='book3', description='desc', isbn='454518')

        response = self.client.get(reverse('books:detail', kwargs={'id': book.id}))
        self.assertContains(response, book.title)
