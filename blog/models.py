# coding=utf-8
from django.db import models
from django.contrib import admin
from DjangoUeditor.models import UEditorField

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'blog'
        verbose_name = '标签'
        verbose_name_plural = '标签'


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta(object):
        app_label = 'blog'
        verbose_name = '分类目录'
        verbose_name_plural = '分类目录'


class Article(models.Model):
    caption = models.CharField(max_length=150)
    publish_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    click = models.IntegerField(default=0)
    content = UEditorField( '内容   ', width=1200, height=600, toolbars="full", imagePath="", filePath="",
                            upload_settings={"imageMaxSize": 1204000}, settings={}, command=None, blank=True)


    def __str__(self):
        return self.caption

    class Meta(object):
        app_label = 'blog'
        verbose_name = '文章'
        verbose_name_plural = '文章'


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('caption', 'publish_time', 'category')
