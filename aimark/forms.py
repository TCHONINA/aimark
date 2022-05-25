from django import forms
from django.contrib.auth.models import User
from django.http import request


class MarqueForm(forms.Form):
    id = forms.IntegerField(label='Id', required=False, widget=forms.HiddenInput)
    title = forms.CharField(label='Title', max_length=100, required=True
                            , widget=forms.TextInput(attrs={'class': 'form-control'}))
    image = forms.ImageField(label='Image',  required=False,
                             widget=forms.FileInput(attrs={'class': 'form-control'}), )
    created_at = forms.DateField(label='Created_at', required=False)

