from django.db import models
from django.core.urlresolvers import reverse
from redactor.fields import RedactorField


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='blog/category/', null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category_posts")

    def post_count(self):
        return self.posts.count()

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Tag(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("tag_posts", kwargs={"slug": self.slug})

    def post_count(self):
        return self.posts.count()

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"


class EntryQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)


class Post(models.Model):
    title = models.CharField(max_length=200)
    featured_image = models.ImageField(upload_to='blog/featured/%Y/%m/%d/', null=True, blank=True)
    body = RedactorField(verbose_name=u'Entry body')
    slug = models.SlugField(max_length=200, unique=True)
    publish = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, related_name='posts')
    category = models.ForeignKey(Category, related_name='posts', null=True, blank=True)

    objects = EntryQuerySet.as_manager()

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("entry_detail", kwargs={"slug": self.slug})

    def featured_image_preview(self):
        if self.featured_image:
            return u'<img src="%s" width="100px" alt="Image Preview">' % (self.featured_image.url)
        else:
            return u'(No Image)'

    featured_image_preview.short_description = 'Image Preview'
    featured_image_preview.allow_tags = True

    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"
        ordering = ["-created"]
