from django.urls import path
from django.contrib import admin

import posts.posts_api.views as v

urlpatterns = [
    path('', v.PostListApiView.as_view(), name='list'),
    path('<int:pk>/', v.PostDetailApiView.as_view(), name='pk_detail'),
    path('create/', v.PostCreateApiView.as_view(), name='create'),
    path('<str:slug>/', v.PostDetailBySlugApiView.as_view(), name='slug_detail'),
    # path('<str:slug>/', post_detail, name='detail'),
    path('<str:slug>/edit/', v.PostUpdateApiView.as_view(), name='update'),
    path('<int:pk>/delete/', v.PostDeleteApiView.as_view(), name='delete'),
]
