from django.contrib.syndication.views import Feed
from blog.models import Entry


class LatestPosts(Feed):
    title = "Blog"
    link = "/feed/"
    description = "Lates Posts"

    def items(self):
        return Entry.objects.published()[:5]
