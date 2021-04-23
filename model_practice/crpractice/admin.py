from django.contrib import admin
from .models import MyClass, MyStudent, Category, Article

# Register your models here.
admin.site.register(MyClass)
admin.site.register(MyStudent)
admin.site.register(Category)
admin.site.register(Article)