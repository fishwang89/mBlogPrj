from django.contrib import admin
from models import ArticleAdmin, Article, Classification

# Register your models here.
admin.site.register(Article, ArticleAdmin)
admin.site.register(Classification)
