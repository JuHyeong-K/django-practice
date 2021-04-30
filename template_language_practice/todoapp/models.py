from django.db import models

# Create your models here.
class Todo(models.Model):
    content = models.CharField(max_length=30)
    is_completed = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)