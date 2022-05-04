from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied, NotFound

from posts.models import Comment, Group, Post
from .serializers import (CommentSerializer, GroupSerializer, PostSerializer)


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied('Изменение чужого контента запрещено!')
        super().perform_update(serializer)

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied('Удаление чужого контента запрещено!')
        super().perform_destroy(instance)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        post = Post.objects.filter(id=self.kwargs.get('post_id'))
        if not post.exists():
            raise NotFound
        serializer.save(
            author=self.request.user,
            post=post.first(),
        )

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied('Изменение чужого контента запрещено!')
        super().perform_update(serializer)

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied('Удаление чужого контента запрещено!')
        super().perform_destroy(instance)

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        if not Post.objects.filter(id=post_id).exists():
            raise NotFound(f'Пост с id {post_id} не существует')
        return Comment.objects.filter(post_id=post_id)
