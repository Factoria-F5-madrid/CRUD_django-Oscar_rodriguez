from django.urls import path
from .views import BooksView

urlpatterns = [
    path('', BooksView.booksList, name="books_list"),
    path('create', BooksView.booksCreate, name="books_create"),
    path('<int:pk>', BooksView.booksDetail, name="books_detail"),
]