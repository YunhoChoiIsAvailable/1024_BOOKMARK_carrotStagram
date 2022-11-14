from django.contrib import admin
from django.urls import path
from bookmark.views import *

app_name = 'bookmark'

urlpatterns = [
    path('', BookmarkLV.as_view()),
    path('defbookmark/', defbookmark, name='defbookmark' ),

    #path('<int:pk>/', BookmarkDV.as_view(), name='detail'),
    path('<int:bookmark_id>/', bookmarkDV, name='detail'),

]
