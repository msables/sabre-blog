from django.contrib import admin
from  blog.models import Post, Tag

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class EntryAdmin(admin.ModelAdmin):
    list_display = ("title", "created")
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ('featured_image_preview', )

admin.site.register(Post, EntryAdmin)
admin.site.register(Tag, TagAdmin)
