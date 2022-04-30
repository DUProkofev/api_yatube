from rest_framework.decorators import action
from rest_framework import viewsets
from .serializers import PostSerializer, GroupSerializer, CommentSerializer
from posts.models import Group, Post, Comment
from django.shortcuts import get_list_or_404


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.kwargs.get("post_id")
        new_queryset = get_list_or_404(Comment, post_id=post_id)
        return new_queryset
