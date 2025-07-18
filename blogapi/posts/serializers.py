# posts/serializers.py
from rest_framework import serializers
from django.contrib.auth import get_user_model  # new

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(  # new
        queryset=get_user_model().objects.all(), slug_field="username"
    )

    class Meta:
        model = Post
        fields = ("id", "author", "title", "body", "created_at")

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id","username",)