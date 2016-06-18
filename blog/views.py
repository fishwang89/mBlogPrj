from django.shortcuts import render, render_to_response
from blog.models import Article

# Create your views here.
def blog_list(request):
    blogs = Article.objects.all().order_by('-publish_time')
    return render_to_response('index.html', {})