"""test1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog import views as blog_views


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mBlogPrj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^ueditor/', include("DjangoUeditor.urls")),
    # url(r'^index/', 'blog.views.index_page'),
    url(r'^index/', blog_views.index_page, name='index_page'),
    url(r'^about/', blog_views.about_page, name='about_page'),
    url(r'^list/(?P<page_num>\d{1,3})/', blog_views.article_list, name='article_list'),
    url(r'^categories/(?P<category_type>\S+)/(?P<page_num>\d{1,3})/', blog_views.article_category_list, name='article_category_list'),
    url(r'^article/(?P<arti_id>\d{1,5})/', blog_views.article, name='article'),
    url(r'^start/(?P<start>\d{1,3})/end/(?P<end>\d{1,3})', blog_views.generate_article, name='generate_article'),
    url(r'^search/', include('haystack.urls')),
)

'''urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mBlogPrj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # url(r'^index/', 'blog.views.index_page'),
    url(r'^index/', 'blog.views.index_page', name='index_page'),
    url(r'^list/(?P<page_num>\d{1,3})/', 'blog.views.article_list', name='article_list'),
    url(r'^categories/(?P<category_type>\S+)/(?P<page_num>\d{1,3})/', 'blog.views.article_category_list', name='article_category_list'),
    url(r'^article/(?P<arti_id>\d{1,5})/', 'blog.views.article', name='article'),
    url(r'^start/(?P<start>\d{1,3})/end/(?P<end>\d{1,3})', 'blog.views.generate_article', name='generate_article'),
)'''
