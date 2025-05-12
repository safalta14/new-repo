from django import forms
from .models import News

class Newsform(forms.ModelForm):
    class Meta:
        model=News
        fields=('title','category','description','image')
