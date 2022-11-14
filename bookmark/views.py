from django.views.generic import *
from bookmark.models import *
from django.shortcuts import render, get_object_or_404


# Create your views here.


class BookmarkLV(ListView):
    model = Bookmark


#class BookmarkDV(DetailView):
#    model = Bookmark

def defbookmark(request):
    bookmark_list = Bookmark.objects.all()
    return render(request, 'bookmark/defbookmark.html', {'bookmark_list': bookmark_list})


def bookmarkDV(request, bookmark_id):
    bookmark = Bookmark.objects.get(pk=bookmark_id)
    #bookmark = get_object_or_404(Bookmark, pk=bookmark_id)
    context = {'object': bookmark}
    return render(request, 'bookmark/bookmark_detail.html', context)
