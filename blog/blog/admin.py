from django.contrib import admin
from .models import Post, Comment

@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = ('title', 'body', 'author', 'date_posted')
    list_filter = ('author', 'title',)
    search_fields = ('date_posted', 'title')
    
    
@admin.register(Comment)
class AdminPost(admin.ModelAdmin):
    list_display = ('post', 'comment', 'comment_author', 'commented_on', 'email')
    list_filter = ('post', 'comment_author',)
    search_fields = ('post', 'comment_author')
