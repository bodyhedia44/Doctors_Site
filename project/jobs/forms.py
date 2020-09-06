from django import forms
from accounts.models import Comment


class AddComment(forms.ModelForm):
    class Meta:
        model=Comment
        fields='__all__'
        exclude=['name','where']