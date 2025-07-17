"""Миксины вьюсетов проекта api."""

from rest_framework import viewsets, exceptions


class AuthorMixin(viewsets.ViewSetMixin):
    """Миксин проверки на автора."""

    def perform_destroy(self, instance):
        """Удаление объекта только для автора."""
        if instance.author != self.request.user:
            raise exceptions.PermissionDenied(
                'Удаление чужого контента запрещено!'
            )
        instance.delete()

    def perform_update(self, serializer):
        """Изменения объекта только для автора."""
        if serializer.instance.author != self.request.user:
            raise exceptions.PermissionDenied(
                'Изменение чужого контента запрещено!'
            )
        serializer.save()
