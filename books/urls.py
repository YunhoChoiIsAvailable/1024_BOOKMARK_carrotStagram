from django.urls import path
from books.views import *

app_name='books'

urlpatterns = [
    #/books/
    path("", BooksModelView.as_view(), name='index'),

    #/books/book/
    path("book/", BookList.as_view(),name='book_list'),
    # /books/author/
    path("author/", AuthorList.as_view(), name='author_list'),
    # /books/publisher/
    path("publisher/", PublisherList.as_view(), name='publisher_list'),
    # /books/book/2/
    path("book/<int:pk>/", BookDetail.as_view(), name='book_detail'),

    path("author/<int:pk>/", AuthorDetail.as_view(), name='author_detail'),

    path("publisher/<int:pk>/", PublisherDetail.as_view(), name='publisher_detail'),
]