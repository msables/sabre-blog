from django.contrib import admin
from  blog.models import Entry, Tag


class EntryAdmin(admin.ModelAdmin):
    list_display = ("title", "created")
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ('featured_image_preview', )

admin.site.register(Entry, EntryAdmin)
admin.site.register(Tag)
