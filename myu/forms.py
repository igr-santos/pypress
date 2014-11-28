from django.contrib.auth.forms import UserCreationForm
from django import forms


class MyUserCreationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta(UserCreationForm.Meta):
        fields = ('username', 'email', 'first_name', 'last_name',
                  'password1', 'password2', 'is_active',)
