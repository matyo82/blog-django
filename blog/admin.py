from django.contrib import admin
from .models import Article, Comment, Tag


class CommentAdmin(admin.StackedInline):
    model = Comment
    extra = 0

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    inlines = [CommentAdmin]
    list_display = [
        'title',
        'body',
        'author',
    ]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'status', 'article')
    list_filter = ['status']

