from django.db import models
from django.contrib.auth.models import User
from behaviors import BaseField


# Create your models here.
class Category(BaseField):
    name = models.CharField(max_length=30)

class Article(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='article')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='article')
    topic = models.CharField(max_length=30)
    content = models.CharField(max_length=100)