from django.conf.urls import patterns, include, url
from blog.views import BlogIndex, BlogDetail
from blog.feed import LatestPosts

urlpatterns = patterns('',
    url(r'^redactor/', include('redactor.urls')),
    url(r'^feed/$', LatestPosts(), name="feed"),
    url(r'^$', BlogIndex.as_view(), name="index"),
    url(r'^(?P<slug>\S+)$', BlogDetail.as_view(), name="entry_detail"),
)
