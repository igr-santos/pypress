from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from .models import Entry


class EntryDetailView(DetailView):
    model = Entry


class EntryListView(ListView):
    queryset = Entry.objects.published()
    paginate_by = 10

    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate_by', self.paginate_by)


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
