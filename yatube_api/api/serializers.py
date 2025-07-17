"""Сериализаторы проекта."""
from rest_framework import serializers

from posts.models import Comment, Group, Post


class GroupSerializer(serializers.ModelSerializer):
    """Сериализатор модели Group."""

    class Meta:
        """Метаданные модели Group."""

        model = Group
        fields = ('id', 'title', 'slug', 'description')


class PostSerializer(serializers.ModelSerializer):
    """Сериализатор модели Post."""

    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        """Метаданные модели Post."""

        model = Post
        fields = ('id', 'text', 'author', 'pub_date')


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор модели Comment."""

    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault(),
    )
    post = serializers.PrimaryKeyRelatedField(
        read_only=True)

    class Meta:
        """Метаданные модели Comment."""

        model = Comment
        fields = ('id', 'text', 'author', 'post', 'created')
