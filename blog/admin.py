from django.contrib import admin

# Register your models here.

from .models.blog import Article
admin.site.register(Article)