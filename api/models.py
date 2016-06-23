from __future__ import unicode_literals
from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)


class Paragraph(models.Model):
    text = models.CharField(max_length=1000)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='paragraphs')


class Comment(models.Model):
    text = models.CharField(max_length=1000)
    paragraph = models.ForeignKey(Paragraph, on_delete=models.CASCADE, related_name='comments')
