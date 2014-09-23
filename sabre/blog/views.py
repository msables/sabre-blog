from django.views import generic
from blog.models import Post, Tag
from django.shortcuts import get_object_or_404

class BlogIndex(generic.ListView):
    queryset = Post.objects.published()
    template_name = "blog/home.html"
    paginate_by = 2


class BlogDetail(generic.DetailView):
    model = Post
    template_name = "blog/post.html"

class TagPostList(generic.ListView):
    model = Tag
    template_name = "blog/home.html"

    def get_queryset(self):
        self.tag = get_object_or_404(Tag, slug=self.kwargs['slug'])
        return self.tag.posts.all()

    def get_context_data(self, **kwargs):
        context = super(TagPostList, self).get_context_data(**kwargs)
        context['tag'] = self.tag
        return context
