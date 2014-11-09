from django.conf.urls import patterns, url
from .views import EntryDetailView, EntryListView

urlpatterns = patterns(
    '',
    url(
        r'^entry/(?P<slug>[\w-]+)/$',
        EntryDetailView.as_view(),
        name='detail-entry'
    ),
    url(r'^$', EntryListView.as_view(), name='list-entry'),
)
