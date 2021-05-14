from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Member(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, related_name='member')
    name = models.CharField(max_length=30)
    content = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
            

class Article(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='article')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='article')
    topic = models.CharField(max_length=30)
    content = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.topic
        

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.SET_NULL, null=True, related_name='comment')
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='comment')
    content = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.content

class RelationShip(models.Model):
    member = models.OneToOneField(User, on_delete=CASCADE, related_name='relationship')
    follower = models.ManyToManyField(User, related_name='following')

    def __str__(self):
        return f'{self.member}'


class Like(models.Model):
    member = models.ManyToManyField(User, related_name='like', blank=True)
    comment = models.OneToOneField(Comment, on_delete=models.CASCADE, related_name='like')

    def __str__(self):
        return f'{self.comment}'

class HashTag(models.Model):
    name = models.CharField(max_length=64)
    article = models.ManyToManyField(Article, related_name='hashtag', blank=True)

    def __str__(self):
        return f'{self.name}'


    