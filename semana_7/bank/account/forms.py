from django import forms
from django.contrib.auth.models import User

class AccountForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.all())
    name = forms.CharField(max_length=100)
    amount = forms.FloatField()
    active = forms.BooleanField()
   
