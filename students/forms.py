from django import forms


class TestForm(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()
