# articles/admin.py
from django.contrib import admin
from .models import Article, Comment # import Article model

class CommentInLine(admin.TabularInline): # inline admin for comments
    model = Comment

class ArticleAdmin(admin.ModelAdmin):
    inlines = [CommentInLine,] # include comments inline in article admin

admin.site.register(Article, ArticleAdmin) # register article model with custom admin
admin.site.register(Comment) # register comment model to admin site