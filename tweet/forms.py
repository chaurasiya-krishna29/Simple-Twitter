from django import forms
from .models import *

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ('text', 'photo')