from django.conf.urls import url
from .views import index, add_blog, add_post

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^blog/add$', add_blog, name='add_blog'),
    url(r'^post/add$', add_post, name='add_post'),
]
