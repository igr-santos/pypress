from django import forms
from core.models import Category, Page
from timezone_field import TimeZoneFormField


class GeneralConfig(forms.Form):
    site_title = forms.CharField(label='Site Title')
    site_desc = forms.CharField(label='Site Description')
    site_url = forms.URLField(label='Site URL')
    site_email = forms.EmailField(label='Site Email',
                                  help_text='This field is only used by '
                                  'system to notify purposes. Like new users.')
    timezone = TimeZoneFormField(label='Timezone')
    register_open = forms.BooleanField(label='Membership - Anyone can '
                                       'register', initial=False,
                                       required=False)


class WriteConfig(forms.Form):
    default_category = forms.ChoiceField(label="Default Category", choices=[])
    github_repository = forms.URLField(
        required=False,
        label='Github Repository',
        help_text='A URL to a git repository '
        'containing the .rst or .md files that will be converted to entries')

    def __init__(self, *args, **kwargs):
        super(WriteConfig, self).__init__(*args, **kwargs)
        qs = Category.objects.all()
        self.fields['default_category'].choices = [(x.pk, x.name) for x in qs]


class ReadConfig(forms.Form):
    HOMEPAGE_CHOICES = [
        ('recent_entries', 'Recent Entries'),
        ('static_page', 'Static Page')
    ]

    homepage = forms.ChoiceField(
        initial='recent_entries',
        choices=HOMEPAGE_CHOICES, widget=forms.RadioSelect())
    homepage_choices = forms.ChoiceField(choices=[])
    entries_per_page = forms.IntegerField(
        initial=10,
        help_text="Numbers of entries per page")

    def __init__(self, *args, **kwargs):
        super(ReadConfig, self).__init__(*args, **kwargs)
        qs = Page.objects.all()
        self.fields['homepage_choices'].choices = [(x.pk, x.title) for x in qs]
