from django.conf.urls import url
from .views import index, add_blog, add_post, remove_blog, remove_post

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^blog/add$', add_blog, name='add_blog'),
    url(r'^post/add$', add_post, name='add_post'),
    url(r'^blog/(?P<_id>[0-9]*)/remove$', remove_blog, name='remove_blog'),
    url(r'^post/(?P<_id>[0-9]*)/remove$', remove_post, name='remove_post'),
]
