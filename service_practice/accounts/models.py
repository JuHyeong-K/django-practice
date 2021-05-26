from django.db import models
from django.contrib.auth.models import User
from behaviors import BaseField
# Create your models here.

class account(BaseField):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='account')
    name = models.CharField(max_length=30, null=True, blank=True)
    content = models.CharField(max_length=100, null=True, blank=True)