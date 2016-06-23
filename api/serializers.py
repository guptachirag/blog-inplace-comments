from rest_framework import serializers
from api import models


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        extra_kwargs = {'paragraph': {'write_only': True}}


class ParagraphSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Paragraph
        exclude = ('post',)


class PostSerializer(serializers.ModelSerializer):
    paragraphs = ParagraphSerializer(many=True)
    class Meta:
        model = models.Post

    def create(self, validated_data):
        paragraphs = validated_data.pop('paragraphs')
        post = models.Post.objects.create(**validated_data)
        for para in paragraphs:
            models.Paragraph.objects.create(post=post, **para)
        return post


class ParagraphCommentSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = models.Paragraph
        exclude = ('post',)


class PostCommentSerializer(serializers.ModelSerializer):
    paragraphs = ParagraphCommentSerializer(many=True)
    class Meta:
        model = models.Post
