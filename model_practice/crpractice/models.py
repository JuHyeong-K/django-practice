from django.db import models

# Create your models here.
class MyClass(models.Model):
    class_num = models.IntegerField()
    lecturer = models.CharField(max_length=30)
    class_room = models.CharField(max_length=30)
    strudents_num = models.IntegerField()

class MyStudents(models.Model):
    name = models.CharField(max_length=30)
    phone_num = models.CharField(max_length=30)
    intro_text = models.TextField()