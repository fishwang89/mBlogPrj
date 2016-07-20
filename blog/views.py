#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article, Classification
from time import time

# Create your views here.


# use to generate dict for theme_base variable
def theme_base(temp_amount=0):
    if temp_amount == 0:
        article_amount = Article.objects.all().count()
    else:
        print "yesyesyes"
        article_amount = temp_amount

    page_amount = article_amount/10 + 1
    pages = range(1, page_amount+1)

    classfications = Classification.objects.all()
    class_count = {}
    for class_type in classfications:
        class_count[class_type.name] = Article.objects.filter(classification__name=class_type.name).count()

    return {'article_amount': article_amount, 'classfications': classfications, 'page_amount': page_amount,
             'pages': pages, 'class_count': class_count}


def index_page(request):
    theme_base_dict = theme_base()
    res_dict = {}
    res_dict.update(theme_base_dict)
    return render(request, 'index.html', res_dict)


def article_list(request, page_num):
    # if page_num == "":
    #    page_num = "1"

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
    res_dict['url_type'] = "article_list"


    return render(request, 'article_list.html', res_dict)


def article_class_list(request, class_type, page_num):
    page = int(page_num)
    articles_per_page = 10

    c_count = Article.objects.filter(classification__name=class_type).count()

    # get base info about article in DB
    theme_base_dict = theme_base(temp_amount=c_count)
    res_dict = {}
    res_dict.update(theme_base_dict)

    # calculate the article_id that will be showed
    article_start = (page-1)*articles_per_page
    article_end = page*articles_per_page

    # get article content
    if res_dict['page_amount'] == page_num:
        blogs = Article.objects.filter(classification__name=class_type).order_by("-publish_time")[article_start:]
    else:
        blogs = Article.objects.filter(classification__name=class_type).order_by("-publish_time")[article_start:article_end]

    res_dict['blogs'] = blogs
    res_dict['current_page'] = page     # user page not page_num they are different type
    res_dict['url_type'] = "article_class_list"
    res_dict['class_type'] = class_type

    return render(request, 'article_list.html', res_dict)


def article(request, arti_id):
    article_id = int(arti_id)

    theme_base_dict = theme_base()
    res_dict = {}
    res_dict.update(theme_base_dict)

    blog = Article.objects.get(id=article_id)
    res_dict['blog'] = blog

    return render(request, 'article.html', res_dict)


def generate_article(request, start, end):
    start_num = int(start)
    end_num = int(end)

    while start_num < end_num:
        p = Article(caption=("article"+str(start_num)), publish_time=time(), update_time=time(),
                    classification=Classification.objects.get(id=1), content=("test content for article "+str(start_num)))
        p.save()
        start_num += 1

    return HttpResponse(request, u"article generate success")
