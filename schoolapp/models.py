from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Question(models.Model):
    question = models.CharField(max_length=1000)
    answer_one = models.CharField(max_length=100)
    answer_two = models.CharField(max_length=100)
    answer_three = models.CharField(max_length=100)
    answer_four = models.CharField(max_length=100)

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
