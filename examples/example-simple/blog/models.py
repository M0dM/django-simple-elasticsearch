from django.db import models
from django.template.defaultfilters import slugify


class Blog(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    blog = models.ForeignKey(Blog)
    slug = models.SlugField()
    title = models.CharField(max_length=50)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.title)

        super(BlogPost, self).save(*args, **kwargs)
