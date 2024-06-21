from django import forms
from .models import Currency

class MyModelForm(forms.ModelForm):
    class Meta:
        model = Currency
        fields = ['status']
