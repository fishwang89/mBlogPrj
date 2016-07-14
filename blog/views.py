#coding=utf-8
from django.shortcuts import render
from blog.models import Article, Classification
from django import forms

# Create your views here.


# use to generate dict for theme_base variable
def theme_base():
    blogs = Article.objects.all().order_by('-publish_time')
    article_amount = blogs.count()
    classfications = Classification.objects.all()
    page_amount = article_amount/10 + 1
    return {'article_amount': article_amount, 'classfications': classfications, 'page_amount': page_amount}


def index_page(request):
    theme_base_dict = theme_base()
    res_dict = {}
    res_dict.update(theme_base_dict)
    return render(request, 'index.html', res_dict)


def article_list(request):
    theme_base_dict = theme_base()
    res_dict = {}
    res_dict.update(theme_base_dict)

    blogs = Article.objects.all().order_by('-publish_time')
    res_dict['blogs'] = blogs

    return render(request, 'article_list.html', res_dict)


def article(request, page_num):
    page = int(page_num)

    theme_base_dict = theme_base()
    res_dict = {}
    res_dict.update(theme_base_dict)

    blogs = Article.objects.all().order_by('-publish_time')
    res_dict['blogs'] = blogs
    res_dict['page'] = page

    return render(request, 'article_list.html', res_dict)
