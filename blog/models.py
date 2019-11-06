from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=500)
    author = models.CharField(max_length=50)
    tags = ArrayField(
        models.CharField(max_length=50)
    )
    body = models.TextField()