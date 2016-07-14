from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mBlogPrj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # url(r'^index/', 'blog.views.index_page'),
    url(r'^index/', 'blog.views.index_page', name='index_page'),
    url(r'^article_list/', 'blog.views.article_list', name="article_list"),
    #url(r'^list/(?P<page>[0-9]+)/$', 'blog.views.article_list', name='article_list'),
    url(r'^list/(\d{1,3})/', 'blog.views.article', name='article'),
)
