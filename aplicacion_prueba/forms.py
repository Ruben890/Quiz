from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegiterForm(UserCreationForm):
    first_name = forms.CharField(label='first name', max_length=150, required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'first_name', 'class': 'form-control'}))

    last_name = forms.CharField(label='last name', max_length=150, required=True,
                                widget=(forms.TextInput(attrs={'placeholder': 'last_name', 'class': 'form-control'})))

    email = forms.EmailField(label="Email", required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control'}))

    username = forms.CharField(label='username', max_length=150, required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}))

    password1 = forms.CharField(label='password', max_length=100, required=True,
                                widget=(forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'})))

    password2 = forms.CharField(label='confirm password', max_length=100, required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'confirm password', 'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email',
                  'username', 'password1', 'password2']
        help_texts = {k: "" for k in fields}
