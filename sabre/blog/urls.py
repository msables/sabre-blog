from django.conf.urls import patterns, url
from blog.views import BlogIndex, BlogDetail
from blog.feed import LatestPosts

urlpatterns = patterns('',
    url(r'^feed/$', LatestPosts(), name="feed"),
    url(r'^$', BlogIndex.as_view(), name="index"),
    url(r'^(?P<slug>\S+)$', BlogDetail.as_view(), name="entry_detail"),
)
