from django.urls import path
from django.contrib import admin

from comments.comments_api.views import (
    CommentListApiView,
    CommentDetailApiView
)

urlpatterns = [
    path('', CommentListApiView.as_view(), name='list'),
    path('<int:pk>/', CommentDetailApiView.as_view(), name='detail'),
    # path('<int:id>/delete/', comment_delete, name='delete'),
]
