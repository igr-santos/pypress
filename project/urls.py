from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^blog/', include('core.urls', namespace='blog')),
    url(r'^comments/', include('django_comments.urls', namespace='comments')),
    url(r'^admin/', include(admin.site.urls)),
)
