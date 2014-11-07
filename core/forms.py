from django import forms
from epiceditor.widgets import AdminEpicEditorWidget
from .models import Entry


class EntryForm(forms.ModelForm):
    body = forms.CharField(widget=AdminEpicEditorWidget())

    class Meta:
        model = Entry
