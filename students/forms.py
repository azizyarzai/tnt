from django import forms
from students.models import Student


def length(val):
    if len(val) > 10:
        raise forms.ValidationError("Length must be less than 10 char.")


class TestForm(forms.Form):
    name = forms.CharField(
        required=False, validators=[length], label="Your Name")
    age = forms.IntegerField()


class StudentModalForm(forms.ModelForm):
    class Meta:
        model = Student
        # fields = ['name', 'date_of_birth']
        fields = '__all__'
        # exclude = ['name']
