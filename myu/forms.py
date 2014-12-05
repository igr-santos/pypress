from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class MyUserCreationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta(UserCreationForm.Meta):
        fields = ('username', 'email', 'first_name', 'last_name',
                  'password1', 'password2', 'groups', 'is_active',)


class MyUserEditForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        fields = ('username', 'email', 'first_name', 'last_name',
                  'groups', 'is_active', 'password')
