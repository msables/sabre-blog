from django.views import generic
from blog.models import Post, Tag


class BlogIndex(generic.ListView):
    queryset = Post.objects.published()
    template_name = "blog/home.html"
    paginate_by = 2


class BlogDetail(generic.DetailView):
    model = Post
    template_name = "post.html"

class TagPostList(generic.ListView):
    def get_queryset(self):
        slug = self.kwargs['slug']
        try:
            tag = Tag.objects.get(slug=slug)
            return tag.post_set.all()
        except Tag.DoesNotExist:
            return Post.objects.none()
