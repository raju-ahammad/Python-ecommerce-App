from django.contrib import admin
from .models import BlogCategory, BlogPost, CommentModel
# Register your models here.

admin.site.register(BlogCategory)



class BlogPostAdmin(admin.ModelAdmin):
    list_display  = ('title', 'slug', 'category', 'author', 'publish', 'created',)
    list_filter = ('title', 'slug',)
    search_fields = ('title', 'slug', 'category',)

admin.site.register(BlogPost, BlogPostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display  = ('post', 'author', 'created_on',)
    search_fields = ('post',)
    list_filter   = ('post',)

admin.site.register(CommentModel, CommentAdmin)
