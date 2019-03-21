from rest_framework import serializers
from posts.models import Post
from comments.comments_api.serializers import CommentSerializer
from comments.models import Comment


class PostListSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='posts_api:pk_detail', lookup_field='pk'
    )
    delete_url = serializers.HyperlinkedIdentityField(
        view_name='posts_api:delete', lookup_field='pk'
    )
    user = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()
    markdown = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()

    def get_comments(self, obj):
        content_type = obj.get_content_type
        object_id = obj.id
        comments_queryset = Comment.objects.filter_by_instance(obj)
        comments = CommentSerializer(comments_queryset, many=True).data
        return comments

    def get_user(self, obj):
        return str(obj.user.username)

    def get_markdown(self, obj):
        return obj.get_markdown()

    def get_image(self, obj):
        try:
            img = obj.image.url
        except:
            img = None
        return img

    class Meta:
        model = Post
        fields = ['url', 'user', 'id', 'title', 'markdown', 'image', 'delete_url', 'comments']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'content', 'publish']


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "title",
            "content",
            "publish",
        ]
