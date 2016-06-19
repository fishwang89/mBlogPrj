from django.db import models
from django.contrib import admin

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
    content = models.TextField()

admin.site.register(Article)
admin.site.register(Classification)
