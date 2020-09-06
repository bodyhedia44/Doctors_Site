from django import forms
from accounts.models import Doctor
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class EditForm(forms.ModelForm):
    class Meta:
        model=Doctor
        fields='__all__'
        exclude=['user']


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']