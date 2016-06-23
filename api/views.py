from django.http import Http404
from django.core.paginator import Paginator

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.models import (
    Post,
)

from api.serializers import (
    PostSerializer,
    CommentSerializer,
    PostCommentSerializer,
)


class PostView(APIView):

    def get(self, request):
        page = request.GET.get('page', 1)
        paginator = Paginator(Post.objects.all(), 5)
        try:
            posts = paginator.page(page)
        except:
            posts = paginator.page(1)

        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentView(APIView):

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetailView(APIView):

    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        post = self.get_object(pk)
        serializer = PostCommentSerializer(post)
        return Response(serializer.data)
