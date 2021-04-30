from django.db import models

# Create your models here.
class MyClass(models.Model):
    num = models.IntegerField()
    lecturer = models.CharField(max_length=30)
    room = models.CharField(max_length=30)
    students_num = models.IntegerField()

    def __str__(self):
        return f"{self.num}"

class MyStudent(models.Model):
    name = models.CharField(max_length=30)
    phone_num = models.CharField(max_length=30)
    intro_text = models.TextField()
    
    def __str__(self):
        return f"{self.name}"

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name}"

class Article(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='articles')
    topic = models.CharField(max_length=30)
    content = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    author = models.CharField(max_length=30)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.topic}"
