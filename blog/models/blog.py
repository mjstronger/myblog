from django.db import models
import django.utils.timezone as timezone
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField("文章标题",max_length=32,default="Title")
    add_date = models.DateTimeField("保存日期",default= timezone.now)
    mod_date = models.DateTimeField("最后修改日期",auto_now= True)
    excerpt = models.CharField("文章摘要",max_length=200, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)