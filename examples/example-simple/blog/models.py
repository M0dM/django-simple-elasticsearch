from django.db import models
from django.db.models.signals import post_save, pre_delete
from django.template.defaultfilters import slugify
from simple_elasticsearch.mixins import ElasticsearchIndexMixin


class Blog(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()

    def __str__(self):
        return self.name


class BlogPost(models.Model, ElasticsearchIndexMixin):
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

    @classmethod
    def get_queryset(cls):
        return BlogPost.objects.all().select_related('blog')

    @classmethod
    def get_index_name(cls):
        return 'blog'

    @classmethod
    def get_type_name(cls):
        return 'posts'

    @classmethod
    def get_type_mapping(cls):
        return {
            "properties": {
                "created_at": {
                    "type": "date",
                    "format": "dateOptionalTime"
                },
                "title": {
                    "type": "string"
                },
                "body": {
                    "type": "string"
                },
                "slug": {
                    "type": "string"
                },
                "blog": {
                    "properties": {
                        "id": {
                            "type": "long"
                        },
                        "name": {
                            "type": "string"
                        },
                        "description": {
                            "type": "string"
                        }
                    }
                }
            }
        }

    @classmethod
    def get_document(cls, obj):
        return {
            'created_at': obj.created_at,
            'title': obj.title,
            'body': obj.body,
            'slug': obj.slug,
            'blog': {
                'id': obj.blog.id,
                'name': obj.blog.name,
                'description': obj.blog.description,
            }
        }

# Update / Delete document from index
# when correponding instance is update / delete from RDBS
post_save.connect(BlogPost.save_handler, sender=BlogPost)
pre_delete.connect(BlogPost.delete_handler, sender=BlogPost)
