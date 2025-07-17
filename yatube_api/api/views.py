"""Вьюсеты эндпоинтов проекта."""
from django.shortcuts import get_object_or_404
from posts.models import Group, Post
from rest_framework import viewsets

from .mixins import AuthorMixin
from .serializers import (
    CommentSerializer,
    GroupSerializer,
    PostSerializer)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет эндпоинта /groups/."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PostViewSet(AuthorMixin, viewsets.ModelViewSet):
    """Вьюсет эндпоинта /posts/."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        """Определяет поле автора при создании объекта."""
        serializer.save(author=self.request.user)


class CommentViewSet(AuthorMixin, viewsets.ModelViewSet):
    """Вьюсет эндпоинта /comments/."""

    serializer_class = CommentSerializer

    def get_current_post(self):
        """Возвращает пост по id."""
        post = get_object_or_404(
            Post,
            id=self.kwargs.get('post_id'),
        )
        return post

    def get_queryset(self):
        """Возвращает все комментарии поста."""
        return self.get_current_post().comments.all()

    def perform_create(self, serializer):
        """Создаёт комментарий к конкретному посту."""
        serializer.save(
            author=self.request.user,
            post=self.get_current_post(),
        )
