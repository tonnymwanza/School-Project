from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Room_details(models.Model):
    host = models.CharField(max_length=255)
    room_name = models.CharField(max_length=255)
    topic = models.CharField(max_length=255)
    room_description = models.TextField()
    members = models.ManyToManyField(User, blank=True, null=True)    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = [
            "created"
        ]