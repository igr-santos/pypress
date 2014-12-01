from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from .models import Entry, Page


class EntryDetailView(DetailView):
    model = Entry


class EntryListView(ListView):
    queryset = Entry.objects.all()
    paginate_by = 10


class EntryCreateView(CreateView):
    model = Entry
    success_url = reverse_lazy('adm:entry-list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class EntryEditView(UpdateView):
    model = Entry
    success_url = reverse_lazy('adm:entry-list')


class PageListView(ListView):
    queryset = Page.objects.all()
    paginate_by = 10


class PageCreateView(CreateView):
    model = Page
    success_url = reverse_lazy('adm:page-list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class PageEditView(UpdateView):
    model = Page
    success_url = reverse_lazy('adm:page-list')
