from django.db import models
from django.contrib.postgres.fields import ArrayField
import datetime
# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=500)
    author = models.CharField(max_length=50)
    tags = ArrayField(
        models.CharField(max_length=50)
    )
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)