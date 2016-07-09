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


class Testform(forms.Form):
    user = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30)


def bootstrap_test(request):
    blogs = Article.objects.all().order_by('-publish_time')
    f = Testform()
    return render(request, 'bootstrap_test.html', {'blogs': blogs, 'form': f})


def static_test(request):
    home = 'abc'
    return render(request, 'static_test.html', {"home":home})