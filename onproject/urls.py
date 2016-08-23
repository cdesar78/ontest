from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create_user', views.create_user, name='create_user'),
    url(r'^log_in', views.log_in, name='log_in'),
    url(r'^main', views.main, name='main'),
    url(r'^post_comment', views.post_comment, name='post_comment'),
    url(r'^like_comment', views.like_comment, name='like_comment'),
    url(r'^unlike_comment', views.unlike_comment, name='unlike_comment'),
    url(r'^logout', views.index, name='logout'),
]