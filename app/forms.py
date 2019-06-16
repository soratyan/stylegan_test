from django import forms

from .models import Touroku

class Indexform(forms.Form):

    namelist = [
        ('妻','妻'),
        ('ひろゆき','ひろゆき'),
    ]

    list1 = [
        ('1','大変不満'),
        ('2','不満'),
        ('3','どちらでもない'),
        ('4','満足'),
        ('5','大変満足'),
    ]

    date = forms.DateField(label="date")
    name = forms.CharField(label="name")
    area = forms.CharField(label="area")
    age = forms.IntegerField(label="age")
    mail = forms.EmailField(label="mail")
    url = forms.URLField(label="url")
    check = forms.BooleanField(label="check",required = False)
    check_null = forms.NullBooleanField(label="check_null")
    choice = forms.ChoiceField(label="感想",choices = list1)
    choice_select = forms.ChoiceField(label="forms.Select",choices = list1,widget=forms.Select(attrs={'size':5}))
    choice_multiple = forms.ChoiceField(label="forms.SelectMultiple",choices = list1,widget=forms.SelectMultiple(attrs={'size':5}))

class IdKensaku(forms.Form):
    id = forms.IntegerField(label = "ID")

class KenkoRecord(forms.ModelForm):
    class Meta:
        model = Touroku
        widgets = {'date':forms.SelectDateWidget}
        fields = ['date','name','bf','lunch','dinner','eatout','drinking','workout','stretch',
        'studying','awaketime','asleeptime','kenkobody','workcond']
        labels = {'date':'日付','name':'氏名'}

class Kensaku(forms.Form):
    findname = forms.CharField(label = "名前",required=False)
    findstatus = forms.CharField(label = "状態",required=False)        
