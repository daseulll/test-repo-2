from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'view_count')


admin.site.register(Post, PostAdmin)
