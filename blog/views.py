# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article, Category, Tag
from time import time

# Create your views here.


# use to generate dict for theme_base variable
def theme_base(temp_amount=0):
    if temp_amount == 0:
        article_amount = Article.objects.all().count()
    else:
        article_amount = temp_amount

    page_amount = article_amount/10 + 1
    pages = range(1, page_amount+1)

    categories = Category.objects.all()
    category_count = {}
    for category_type in categories:
        category_count[category_type.name] = Article.objects.filter(category__name=category_type.name).count()

    tag = Tag.objects.all()
    tags = []
    for tag_unit in tag:
        tags.append(tag_unit)

    return {'article_amount': article_amount, 'categories': categories, 'page_amount': page_amount,
             'pages': pages, 'category_count': category_count, 'tags': tags}


def index_page(request):
    theme_base_dict = theme_base()
    res_dict = {}
    res_dict.update(theme_base_dict)
    return render(request, 'index.html', res_dict)


def about_page(request):
    theme_base_dict = theme_base()
    res_dict = {}
    res_dict.update(theme_base_dict)
    return render(request, 'about.html', res_dict)


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


def article_category_list(request, category_type, page_num):
    page = int(page_num)
    articles_per_page = 10

    c_count = Article.objects.filter(category__name=category_type).count()

    # get base info about article in DB
    theme_base_dict = theme_base(temp_amount=c_count)
    res_dict = {}
    res_dict.update(theme_base_dict)

    # calculate the article_id that will be showed
    article_start = (page-1)*articles_per_page
    article_end = page*articles_per_page

    # get article content
    if res_dict['page_amount'] == page_num:
        blogs = Article.objects.filter(category__name=category_type).order_by("-publish_time")[article_start:]
    else:
        blogs = Article.objects.filter(category__name=category_type).order_by("-publish_time")[article_start:article_end]

    res_dict['blogs'] = blogs
    res_dict['current_page'] = page     # user page not page_num they are different type
    res_dict['url_type'] = "article_category_list"
    res_dict['category_type'] = category_type

    return render(request, 'article_list.html', res_dict)


def article(request, arti_id):
    article_id = int(arti_id)

    theme_base_dict = theme_base()
    res_dict = {}
    res_dict.update(theme_base_dict)

    # in case user request the unavailable page
    if article_id > res_dict['article_amount']:
        article_id = res_dict['article_amount']

    blog = Article.objects.get(id=article_id)
    res_dict['blog'] = blog
    res_dict['current_id'] = article_id

    # 有bug 不能这么用 一次访问可能多次调用这个函数
    print "fwaehfhwaehfwahfuia67890"
    old_hits = int(blog.click)
    new_hits = old_hits + 1
    Article.objects.filter(id=article_id).update(click=new_hits)

    if res_dict['current_id'] < res_dict['article_amount']:
        res_dict['next_id'] = article_id + 1
        res_dict['next_caption'] = Article.objects.get(id=res_dict['next_id'])

    if article_id > 1:
        res_dict['pre_id'] = article_id - 1
        res_dict['pre_caption'] = Article.objects.get(id=res_dict['pre_id'])

    return render(request, 'article.html', res_dict)


def generate_article(request, start, end):
    start_num = int(start)
    end_num = int(end)

    while start_num < end_num:
        p = Article(caption=("article"+str(start_num)), publish_time=time(), update_time=time(),
                    category=Category.objects.get(id=1), content=("test content for article "+str(start_num)))
        p.save()
        start_num += 1

    return HttpResponse(request, u"article generate success")
