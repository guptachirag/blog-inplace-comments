from django.conf.urls import url

from web import views

app_name = 'web'
urlpatterns = [
    url('^$', views.home, name='posts'),
]
