from django.contrib import admin
from django.urls import path
from carrotStagram.views import *

app_name = 'carrotstagram'

urlpatterns = [
    path('', login, name='login'),
    # path('friend', , name='friend'),
]
