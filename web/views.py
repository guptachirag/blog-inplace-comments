from django.shortcuts import render
from rest_framework.decorators import api_view

from api.daos import PostDAO

@api_view(['GET'])
def home(request):
    posts = PostDAO().get_posts(request.GET)
    return render(request, 'web/posts.html', context={'posts': posts})
