from rest_framework import serializers
from posts.models import Comment, Group, Post


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = (
            'id',
            'text',
            'author',
            'image',
            'group',
            'pub_date',
        )


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = (
            'id',
            'title',
            'slug',
            'description',
        )


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = (
            'id',
            'text',
            'author',
            'post',
            'created'
        )
