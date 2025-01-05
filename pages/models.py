from django.db import models
from django.utils.text import slugify
from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    summary = models.CharField(max_length=250)
    image = models.ImageField(upload_to='services/')
    slug = models.SlugField(max_length=200, unique=True)
    icon_class = models.CharField(max_length=100, help_text="مثال: bi-diagram-3", default="bi-diagram-3")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Team(models.Model):
    image = models.ImageField(upload_to='teams/')
    full_name = models.CharField(max_length=150)
    job = models.CharField(max_length=150, default='Team work')
    description = models.TextField()

    def __str__(self):
        return self.full_name
