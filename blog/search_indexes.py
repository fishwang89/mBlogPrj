#coding=utf-8
from blog.models import Article
from haystack import indexes

# Add your code here.


class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='caption')

    def get_model(self):
        return Article

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()   #确定在建立索引时有些记录被索引，这里我们简单地返回所有记录
