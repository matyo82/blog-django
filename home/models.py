from django.db import models

# Create your models here.
class Todo(models.Model):
    titel = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField()