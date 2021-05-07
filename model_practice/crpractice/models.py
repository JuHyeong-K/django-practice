from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30)

class Member(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, related_name='member')
    name = models.CharField(max_length=30)
    content = models.CharField(max_length=100)

class Article(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='article')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='article')
    topic = models.CharField(max_length=30)
    content = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.SET_NULL, null=True, related_name='comment')
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='comment')
    content = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    is_deleted = models.BooleanField(default=False)