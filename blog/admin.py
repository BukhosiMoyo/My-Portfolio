from django.contrib import admin

from .models import Post, Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status')
    ordering = ('status', 'publish')
    raw_id_fields = ('author',)



admin.site.register(Category)

