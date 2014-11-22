from django.conf.urls import patterns, url
from django.contrib.auth.views import login
from django.contrib.auth.decorators import login_required
from core.views import (EntryCreateView, EntryEditView, EntryListView)
from .views import Index


urlpatterns = patterns(
    '',
    url(r'^login/$', login, {'template_name': 'adm/login.html'},
        name='login'),
    url(r'^entries/$', login_required(EntryListView.as_view()),
        name='entry-list'),
    url(r'^entry/$', login_required(EntryCreateView.as_view()),
        name='entry-new'),
    url(r'^entry/(?P<pk>[\w-]+)/$', login_required(EntryEditView.as_view()),
        name='entry-edit'),
    url(r'^$', Index.as_view(), name='index'),
)
