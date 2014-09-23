from django.conf.urls import patterns, url
from blog.views import BlogIndex, BlogDetail, TagPostList
from blog.feed import LatestPosts

urlpatterns = patterns('',
    url(r'^feed/$', LatestPosts(), name="feed"),
    url(r'^$', BlogIndex.as_view(), name="index"),
    url(r'^(?P<slug>[a-zA-Z0-9-]+)$', BlogDetail.as_view(), name="entry_detail"),
    url(r'^tag/(?P<slug>[a-zA-Z0-9-]+)/?$', TagPostList.as_view(), name="tag_posts"),
)
