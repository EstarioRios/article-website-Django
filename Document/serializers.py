from rest_framework.serializers import ModelSerializer
from .models import Blog, Comment


class BlogFullSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"


class BlogListSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = ["title", "description", "tags"]


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
