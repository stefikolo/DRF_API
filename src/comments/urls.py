from django.urls import path
from django.contrib import admin

from comments.views import (
    comment_thread,
    comment_delete

    )

urlpatterns = [
    path('<int:id>/', comment_thread, name='thread'),
    path('<int:id>/delete/', comment_delete, name='delete'),
]
