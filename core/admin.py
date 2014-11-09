from django.contrib import admin
from .models import Entry
from .forms import EntryForm


class EntryAdmin(admin.ModelAdmin):
    form = EntryForm
    list_display = ('title', 'author', 'created_at', 'published_at', 'status')

    def save_model(self, request, entry, form, change):
        entry.author = request.user
        entry.save()

admin.site.register(Entry, EntryAdmin)
