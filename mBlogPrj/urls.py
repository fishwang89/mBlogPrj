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
    url(r'^list/(?P<page_num>\d{1,3})/', 'blog.views.article_list', name='article_list'),
    url(r'^categories/(?P<class_type>\S+)/(?P<page_num>\d{1,3})/', 'blog.views.article_class_list', name='article_class_list'),
    url(r'^article/(?P<arti_id>\d{1,5})/', 'blog.views.article', name='article'),
    url(r'^start/(?P<start>\d{1,3})/end/(?P<end>\d{1,3})', 'blog.views.generate_article', name='generate_article'),
)

