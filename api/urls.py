from django.conf.urls import url

from api import views

urlpatterns = [
    url('^posts/$', views.PostView.as_view()),
    url('^posts/(?P<pk>[0-9]+)$', views.PostDetailView.as_view()),
    url('^comments/$', views.CommentView.as_view()),
]


