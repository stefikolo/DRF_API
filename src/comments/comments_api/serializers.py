from rest_framework import serializers
from comments.models import Comment


def create_comment_serializer(type='post', slug=None, parent_id=None):
    pass


class CommentSerializer(serializers.ModelSerializer):
    reply_count = serializers.SerializerMethodField()

    def get_reply_count(self, obj):
        if obj.is_parent:
            return obj.children().count()
        return 0

    class Meta:
        model = Comment

        fields = [
            # 'user',
            'id',
            'reply_count',
            'content_type',
            'object_id',
            # 'content_object',
            'parent',
            'content'
            # 'timestamp'
        ]


class CommentChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'id',
            'content',
            'timestamp'
        ]


class CommentDetailSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()

    def get_replies(self, obj):
        if obj.is_parent:
            return CommentChildSerializer(obj.children(), many=True).data
        return None

    class Meta:
        model = Comment
        fields = [
            # 'user',
            'id',
            'replies',
            'content_type',
            'object_id',
            # 'content_object',
            'parent',
            'content'
            # 'timestamp'
        ]
