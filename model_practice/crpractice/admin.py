from django.contrib import admin
from .models import Category, Article, Member, Comment, RelationShip, Like, HashTag

# Register your models here.
admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Member)
admin.site.register(Comment)
admin.site.register(RelationShip)
admin.site.register(Like)
admin.site.register(HashTag)