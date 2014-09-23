from blog.models import Category

def categories_list(request):
    return {'categories_list': Category.objects.all()}
