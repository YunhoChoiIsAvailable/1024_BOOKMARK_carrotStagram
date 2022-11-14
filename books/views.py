from django.shortcuts import render
from django.views.generic import *
from books.models import *


# Create your views here.
class BooksModelView(TemplateView):
    template_name = 'books/index.html'

    # template_name='books/base_books.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_list'] = ['Book', 'Author', 'Publisher']
        return context


class ProjectHome(TemplateView):
    template_name = 'home.html'


class BookList(ListView):
    model = Book


class AuthorList(ListView):
    model = Author


class PublisherList(ListView):  # object_list로 html에 넘어갑니다
    model = Publisher


class BookDetail(DetailView):  # object로 넘어간다
    model = Book

class AuthorDetail(DetailView):  # object로 넘어간다
    model = Author

class PublisherDetail(DetailView):  # object로 넘어간다
    model = Publisher