from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Entry, Page


class EntryDetailView(DetailView):
    model = Entry


class EntryListView(ListView):
    queryset = Entry.objects.published()
    paginate_by = 10


class PageDetailView(DetailView):
    model = Page


class PageListView(ListView):
    queryset = Page.objects.published()
    paginate_by = 10
