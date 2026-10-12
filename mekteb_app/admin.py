from django.contrib import admin

from .models import BlogPost, Muellim, Telebe


admin.site.register(Muellim)
admin.site.register(Telebe)


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "is_published")
    list_filter = ("is_published", "created_at")
    search_fields = ("title", "content")
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ("created_at", "updated_at")
