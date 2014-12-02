from django import forms
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
