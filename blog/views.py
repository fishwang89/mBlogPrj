#coding=utf-8
from django.shortcuts import render
from blog.models import Article
from django import forms

# Create your views here.


def index_page(request):
    blogs = Article.objects.all().order_by('-publish_time')
    return render(request, 'index.html', {"blogs": blogs})


def index_article(request):
    blogs = Article.objects.all().order_by('-publish_time')
    print blogs
    return render(request, 'index_article.html', {"blogs": blogs})


def article(request, article_id):
    blogs = Article.objects.all().order_by('-publish_time')
    print blogs
    return render(request, 'index_article.html', {"blogs": blogs})
    
