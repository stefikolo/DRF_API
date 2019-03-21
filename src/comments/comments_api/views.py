from django.db.models import Q
from django.shortcuts import render

from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView, \
    RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination

from posts.posts_api.permissions import IsOwnerOrReadOnly
from posts.posts_api.pagination import PostLimitOffsetPagination, PostPageNumberPagination

from comments.models import Comment

from comments.comments_api.serializers import CommentSerializer, CommentDetailSerializer


class CommentListApiView(ListAPIView):
    # queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [AllowAny]
    filter_backends = [SearchFilter]
    search_fields = ['content', 'user__first_name', 'user__last_name']
    pagination_class = PostPageNumberPagination

    def get_queryset(self, *args, **kwargs):
        query = self.request.GET.get("q")
        queryset_list = Comment.objects.all()
        if query:
            queryset_list = queryset_list.filter(
                Q(content__icontains=query) |
                Q(user__first_name__icontains=query) |
                Q(user__last_name__icontains=query)
            ).distinct()
        return queryset_list


# class CommentCreateApiView(CreateAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = PostCreateSerializer
#     permission_classes = [IsAuthenticated]
#
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)


# class CommentUpdateApiView(RetrieveUpdateAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = PostSerializer
#     lookup_field = 'slug'
#     permission_classes = [IsOwnerOrReadOnly]
#
#     def perform_update(self, serializer):
#         serializer.save(user=self.request.user)
#
#
# class CommentDeleteApiView(DestroyAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = PostSerializer
#     lookup_field = 'slug'
#     permission_classes = [IsAdminUser]


class CommentDetailApiView(RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDetailSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]



