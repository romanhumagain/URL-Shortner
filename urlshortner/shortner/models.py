from django.db import models

class Url(models.Model):
    link = models.URLField(max_length=10000)
    uuid = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True , null=True)
    updated_at = models.DateTimeField(auto_now=True , null=True)
