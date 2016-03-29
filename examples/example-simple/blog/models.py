from django.db import models


class Blog(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()


class BlogPost(models.Model):
    blog = models.ForeignKey(Blog)
    slug = models.SlugField()
    title = models.CharField(max_length=50)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
