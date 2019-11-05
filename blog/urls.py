from django.urls import path,include
import blog.views

urlpatterns = [
    path('content',blog.views.article_content),
    path('index',blog.views.get_index_page ),   
         ]