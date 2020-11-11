from django.contrib import admin

from .models import Post, Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'status')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('status', 'publish_date')
    raw_id_fields = ('author',)



admin.site.register(Category)

