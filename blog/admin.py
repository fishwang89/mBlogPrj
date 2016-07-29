from django.contrib import admin
from models import ArticleAdmin, Article, Category, Tag

# Register your models here.
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Tag)
