from django import forms
from .models import Url

class UrlForm(forms.Form):
    url = forms.URLField(
        max_length=1000,
        widget=forms.TextInput(attrs={'class': 'custom-input-class'}),
    )
