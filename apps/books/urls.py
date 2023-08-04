from django.urls import path

from apps.books.views import homePage, BooksListView, BookDetailView

app_name = 'books'

urlpatterns = [
    path('', homePage, name='home'),
    path('books/', BooksListView.as_view(), name='books'),
    path('detail/<int:id>/', BookDetailView.as_view(), name='detail'),
]