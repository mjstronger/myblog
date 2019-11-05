from django.shortcuts import render

from django.http import HttpResponse
from blog.models.blog import Article
# Create your views here.


def article_content(request):
    article = Article.objects.all()[0]
    title = article.title
    excerpt = article.excerpt
    content = article.content
    article_id = article.id
    add_date = article.add_date
    return_str = 'title: %s, excerpt: %s,'\
        'content: %s, article_id: %s, add_date: %s' % (title,
                                                       excerpt,
                                                       content,
                                                       article_id,
                                                       add_date,)
    return HttpResponse(return_str)


def get_index_page(request):
    all_article = Article.objects.all()
    return render(request,'blog/index.html',
                  {
                      'article_list':all_article
                      }
                  )
