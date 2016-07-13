from django.conf.urls import url

from api import views

app_name = 'api'
urlpatterns = [
    url('^posts/$', views.PostView.as_view(), name="posts"),
    url('^posts/(?P<pk>[0-9]+)$', views.PostDetailView.as_view(), name="post"),
    url('^comments/$', views.CommentView.as_view(), name="comments"),
]


