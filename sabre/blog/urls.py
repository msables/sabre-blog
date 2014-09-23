from django.conf.urls import patterns, url
from blog.views import BlogIndex, BlogDetail, TagPostList, CategoryPostList
from blog.feed import LatestPosts

urlpatterns = patterns('',
    # Blog index page
    url(
        r'^$',
        BlogIndex.as_view(),
        name="blog_index"
    ),

    url(
        r'^feed/$',
        LatestPosts(),
        name="feed"
    ),

    url(
        r'^(?P<slug>[a-zA-Z0-9-]+)$',
        BlogDetail.as_view(),
        name="post_detail"
    ),

    url(r'^tag/(?P<slug>[a-zA-Z0-9-]+)/?$',
        TagPostList.as_view(),
        name="tag_posts"
    ),

    url(r'^category/(?P<slug>[a-zA-Z0-9-]+)/?$',
        CategoryPostList.as_view(),
        name="category_posts"
    ),
)
