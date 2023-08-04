from .models import Book
from django.shortcuts import render
from django.views.generic import ListView
from django.views import View
from django.http import HttpResponse


def homePage(request):
    return render(request, 'index.html', {})


class BooksListView(ListView):
    queryset = Book.objects.all()
    template_name = 'books/bookslist.html'


class BookDetailView(View):
    def get(self, requset, id):
        try:
            book = Book.objects.get(id=id)
        except Book.DoesNotExist:
            return HttpResponse('bunday kitob mavjud emas', status=404)
        return render(requset, 'books/detail.html', {"book": book})