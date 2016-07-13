from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mBlogPrj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # url(r'^index/', 'blog.views.index_page'),
    url(r'^index/', 'blog.views.index_article'),
    url(r'^list/(?P<list_type>/S+)/(?P<page>[0-9]+)/$', views.article_list, name='article_list'),
)
