from django.db.models import Q
from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView, \
    RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from posts.models import Post
from posts.posts_api.serializers import PostSerializer, PostCreateSerializer, PostListSerializer
from posts.posts_api.permissions import IsOwnerOrReadOnly
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from posts.posts_api.pagination import PostLimitOffsetPagination, PostPageNumberPagination


class PostListApiView(ListAPIView):
    # queryset = Post.objects.all()
    serializer_class = PostListSerializer
    permission_classes = [AllowAny]
    filter_backends = [SearchFilter]
    search_fields = ['title', 'content', 'user__first_name', 'user__last_name']
    pagination_class = PostPageNumberPagination

    def get_queryset(self, *args, **kwargs):
        query = self.request.GET.get("q")
        queryset_list = Post.objects.all()
        if query:
            queryset_list = queryset_list.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(user__first_name__icontains=query) |
                Q(user__last_name__icontains=query)
            ).distinct()
        return queryset_list


class PostCreateApiView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostUpdateApiView(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'
    permission_classes = [IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class PostDeleteApiView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'
    permission_classes = [IsAdminUser]


class PostDetailApiView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]


class PostDetailBySlugApiView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly]
