from django.urls import path

from apps.books.views import homePage

app_name = 'books'

urlpatterns = [
    path('', homePage)
]