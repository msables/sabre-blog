from django.views import generic
from blog.models import Entry


class BlogIndex(generic.ListView):
    queryset = Entry.objects.published()
    template_name = "home.html"
    paginate_by = 2


class BlogDetail(generic.DetailView):
    model = Entry
    template_name = "post.html"
