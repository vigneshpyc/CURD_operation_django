from django import forms

class userForms(forms.Form):
   name = forms.CharField(max_length=100)
   Age = forms.IntegerField()