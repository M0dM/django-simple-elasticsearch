from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include('blog.urls', namespace='blog')),
    url(r'^admin/', admin.site.urls),
]

# Only required for debug toolbar
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += url(r'^__debug__/', debug_toolbar.urls),
