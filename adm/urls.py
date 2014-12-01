from django.conf.urls import patterns, url
from django.contrib.auth.views import login, logout
from django.contrib.auth.decorators import login_required
from core.views import (EntryCreateView, EntryEditView, EntryListView,
                        PageCreateView, PageEditView, PageListView)
from myu.views import (UserCreateView, UserEditView, UserListView)
from .views import Index


urlpatterns = patterns(
    '',
    url(r'^login/$', login, {'template_name': 'adm/login.html'},
        name='login'),
    url(r'^logout/$', logout, {'next_page': 'adm:index'},
        name='logout'),

    #user
    url(r'^users/$', login_required(UserListView.as_view()),
        name='user-list'),
    url(r'^user/$', login_required(UserCreateView.as_view()),
        name='user-new'),
    url(r'^user/(?P<pk>[\w-]+)/$', login_required(UserEditView.as_view()),
        name='user-edit'),

    #entries
    url(r'^entries/$', login_required(EntryListView.as_view()),
        name='entry-list'),
    url(r'^entry/$', login_required(EntryCreateView.as_view()),
        name='entry-new'),
    url(r'^entry/(?P<pk>[\w-]+)/$', login_required(EntryEditView.as_view()),
        name='entry-edit'),

    #pages
    url(r'^pages/$', login_required(PageListView.as_view()),
        name='page-list'),
    url(r'^page/$', login_required(PageCreateView.as_view()),
        name='page-new'),
    url(r'^page/(?P<pk>[\w-]+)/$', login_required(PageEditView.as_view()),
        name='page-edit'),

    url(r'^$', Index.as_view(), name='index'),
)
