from django.contrib import admin
from .models import MyClass, MyStudents

# Register your models here.
admin.site.register(MyClass)
admin.site.register(MyStudents)