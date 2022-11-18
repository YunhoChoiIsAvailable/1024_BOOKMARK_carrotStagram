from django.contrib import admin
from django.urls import path
from carrotStagram.views import *

app_name = 'carrotstagram'

urlpatterns = [
    path('', loginView, name='login'),
    # path('/settings', settingView(), name='setting'),
    path('friend/', FriendView.as_view() , name='friend'),
    path('mypage/',MyPageView.as_view(), name='mypage'),
    path('postdetail/<int:pk>/', PostDetailView.as_view(), name='postdetail'),
    path('following/', FollowingView.as_view(), name='following'),
    path('follower/', FollowerView.as_view(), name='follower'),
    path('feed/', FeedView.as_view(), name='feed'),
]
