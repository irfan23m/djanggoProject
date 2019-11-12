from django import forms
from tabungan.models import User 

class formUser(forms.Form):
    userName = forms.CharField()
    fullName = forms.CharField()
    address  = forms.CharField(widget=forms.Textarea)
    dateReg = forms.DateField(widget=forms.SelectDateWidget)
    exp = forms.FloatField()
    level = forms.FloatField()

class newUserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ['fullName', 'address']