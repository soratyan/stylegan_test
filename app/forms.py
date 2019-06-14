from django import forms

class Indexform(forms.Form):
    date = forms.DateField(label="date")
    name = forms.CharField(label="name")
    area = forms.CharField(label="area")
    age = forms.IntegerField(label="age")
    mail = forms.EmailField(label="mail")
    url = forms.URLField(label="url")
