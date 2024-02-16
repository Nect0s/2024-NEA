from django.forms import ModelForm
from django import forms
from members.models import users

#class create_user_form(ModelForm):
    #username = forms.TextInput()
    #password = forms.TextInput()
    #email = forms.TextInput()
    #gender = forms.TextInput()
    #country = forms.TextInput()
    #class Meta:
        #model = users
        #fields = ['username']
        #fields = ['username', 'password', 'email', 'gen', 'country']

class create_user_form(forms.Form):
    username = forms.CharField(label="Enter first name",max_length=50)
    

form = create_user_form()