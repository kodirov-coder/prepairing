from django.contrib.auth.forms import AuthenticationForm
from django import forms

from .models import Users


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control py-4",
        "placceholder": "Foydalanuvchi nomini kiriting!"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control py-4",
        "placceholder": "Parolni kiriting!"
    }))
    class Meta:
        model = Users
        fields = ('username', 'password')