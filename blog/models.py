from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils.text import slugify


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    image = models.ImageField(upload_to='articles/')
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    body = models.TextField()
    summary = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name='articles')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug': self.slug})


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment = models.CharField(max_length=140)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.comment
