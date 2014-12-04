from django.conf.urls import patterns, url
from django.contrib.auth.views import login, logout

from myu.views import (UserCreateView, UserEditView, UserListView)
from .views import (Index,
                    CategoryListView, CategoryCreateView, CategoryEditView,
                    EntryCreateView, EntryEditView, EntryListView,
                    PageCreateView, PageEditView, PageListView,
                    GeneralConfigView, WriteConfigView)

urlpatterns = patterns(
    '',
    url(r'^login/$', login, {'template_name': 'adm/login.html'},
        name='login'),
    url(r'^logout/$', logout, {'next_page': 'adm:index'},
        name='logout'),

    #user
    url(r'^users/$', UserListView.as_view(),
        name='user-list'),
    url(r'^user/$', UserCreateView.as_view(),
        name='user-new'),
    url(r'^user/(?P<pk>[\w-]+)/$', UserEditView.as_view(),
        name='user-edit'),

    #categories
    url(r'^categories/$', CategoryListView.as_view(),
        name='category-list'),
    url(r'^category/$', CategoryCreateView.as_view(),
        name='category-new'),
    url(r'^category/(?P<pk>[\w-]+)/$', CategoryEditView.as_view(),
        name='category-edit'),

    #entries
    url(r'^entries/$', EntryListView.as_view(),
        name='entry-list'),
    url(r'^entry/$', EntryCreateView.as_view(),
        name='entry-new'),
    url(r'^entry/(?P<pk>[\w-]+)/$', EntryEditView.as_view(),
        name='entry-edit'),

    #pages
    url(r'^pages/$', PageListView.as_view(),
        name='page-list'),
    url(r'^page/$', PageCreateView.as_view(),
        name='page-new'),
    url(r'^page/(?P<pk>[\w-]+)/$', PageEditView.as_view(),
        name='page-edit'),

    #configs
    url(r'^config/general$', GeneralConfigView.as_view(),
        name='config-general'),
    url(r'^config/write$', WriteConfigView.as_view(),
        name='config-write'),


    url(r'^$', Index.as_view(), name='index'),
)
