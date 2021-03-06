"""Defines URL patterns for blogs."""
from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'blogs'

urlpatterns = [
    #Home Page
    path('', views.index, name='index'),

    #All Posts
    path('posts/', views.PostList.as_view(), name='home'),

    #All Comments
    url(r'^posts/(?P<post_id>\d+)/$', views.post_comments, name='post_detail'),

    #page for adding a new comment
    url(r'^new_comment/(?P<post_id>\d+)/$', views.new_comment, name='new_comment'),

    #page for all replies
    url(r'^replies/(?P<comment_id>\d+)/$', views.replies, name='replies'),

    #Page for adding reply
    url(r'^reply/(?P<comment_id>\d+)/$', views.reply, name='reply'),

]