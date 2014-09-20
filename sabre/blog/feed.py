from django.contrib.syndication.views import Feed
from blog.models import Post


class LatestPosts(Feed):
    title = "Blog"
    link = "/feed/"
    description = "Lates Posts"

    def items(self):
        return Post.objects.published()[:5]
