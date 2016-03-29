from django.conf.urls import patterns, url
from .views import index

urlpatterns = [
  url(r'^$', index, name='index'),
]
