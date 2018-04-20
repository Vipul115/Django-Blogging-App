from django.contrib import admin

# Register your models here.

from .models import Post

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title", "updated"]
    list_display_links = ["title"]
    list_filter = ["title"]

    class Meta:
        model = Post


admin.site.register(Post, PostModelAdmin)