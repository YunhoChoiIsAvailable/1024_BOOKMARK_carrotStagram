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
    path('setting/', settingView, name='setting'),

    #좋아요, 댓글 기능 구현에 필요
    path('post/like/<int:pk>', post_like, name='post_like'),
    path('comment/like/<int:pk>', comment_like, name='comment_like'),
    path('commend/add/<int:pk>', comment_add, name='comment_add'),

    #로그아웃
    path('logout/', logout, name='logout')
]
