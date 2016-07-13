from django.core.paginator import Paginator

from api.models import Post


class PostDAO:
    def get_posts(self, params):
        page = params.get('page', 1)
        paginator = Paginator(Post.objects.all(), 5)
        posts = paginator.page(page)
        return posts
