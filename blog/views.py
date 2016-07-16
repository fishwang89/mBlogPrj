#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article, Classification
from time import time

# Create your views here.


# use to generate dict for theme_base variable
def theme_base():
    article_amount = Article.objects.all().count()
    classfications = Classification.objects.all()
    page_amount = article_amount/10 + 1
    pages = range(1, page_amount+1)
    return {'article_amount': article_amount, 'classfications': classfications, 'page_amount': page_amount, 'pages': pages}


def index_page(request):
    theme_base_dict = theme_base()
    res_dict = {}
    res_dict.update(theme_base_dict)
    return render(request, 'index.html', res_dict)


def article_list(request, page_num):
    page = int(page_num)
    articles_per_page = 10

    # get base info about article in DB
    theme_base_dict = theme_base()
    res_dict = {}
    res_dict.update(theme_base_dict)

    # calculate the article_id that will be showed
    article_start = (page-1)*articles_per_page
    article_end = page*articles_per_page

    # get article content
    if res_dict['page_amount'] == page_num:
        blogs = Article.objects.order_by('-publish_time')[article_start:]
    else:
        blogs = Article.objects.order_by('-publish_time')[article_start:article_end]

    res_dict['blogs'] = blogs
    res_dict['current_page'] = page     # user page not page_num they are different type

    return render(request, 'article_list.html', res_dict)


def article(request, article_id):
    page = int(article_id)

    theme_base_dict = theme_base()
    res_dict = {}
    res_dict.update(theme_base_dict)

    blogs = Article.objects.all().order_by('-publish_time')
    res_dict['blogs'] = blogs
    res_dict['page'] = page

    return render(request, 'article_list.html', res_dict)


def generate_article(request, start, end):
    start_num = int(start)
    end_num = int(end)

    while start_num < end_num:
        p = Article(caption=("article"+str(start_num)), publish_time=time(), update_time=time(),
                    classification=Classification.objects.get(id=1), content=("test content for article "+str(start_num)))
        p.save()
        start_num += 1

    return HttpResponse(request, u"article generate success")
