from django.db import models
from django.contrib import admin
from DjangoUeditor.models import UEditorField

# Create your models here.


class Classification(models.Model):
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name


class Article(models.Model):
    caption = models.CharField(max_length=150)
    publish_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now_add=True)
    classification = models.ForeignKey(Classification)
    # content = models.TextField()
    content = UEditorField( u'neirong   ', width=1200, height=600, toolbars="full", imagePath="", filePath="",
                            upload_settings={"imageMaxSize": 1204000}, settings={}, command=None, blank=True)

    def __unicode__(self):
        return self.caption

    class Meta(object):
        verbose_name = u'Article'
        verbose_name_plural = u'Articles'


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('caption', 'publish_time', 'classification')
