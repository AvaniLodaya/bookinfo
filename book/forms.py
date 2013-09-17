from django import forms

class Search_ISBN(forms.Form):
    isbn = forms.CharField(max_length=20)
