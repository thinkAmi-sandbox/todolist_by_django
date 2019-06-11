from django.db import models
from django.utils import timezone


class ToDo(models.Model):
    title = models.CharField('タイトル', max_length=50)
    content = models.TextField('内容')
    priority = models.IntegerField('優先度')

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
