from django.urls import path

from apps.books.views import BookListsApiView, BookDetailAPIView

app_name = 'books'

urlpatterns = [
    path('', BookListsApiView.as_view(), name='home'),
    path('<int:id>/', BookDetailAPIView.as_view(), name='books'),
    # path('detail/<int:id>/', BookDetailView.as_view(), name='detail'),
]