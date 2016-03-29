from factory.django import DjangoModelFactory
from pytest_factoryboy import register


@register
class BlogFactory(DjangoModelFactory):

    class Meta:
        model = 'blog.Blog'

    name = 'Test blog'
    description = 'Blog description'
