# In forms.py
from django import forms
from django.contrib.auth.models import users
from django.forms import ModelForm

class CreateUserForm(ModelForm):
    class Meta:
        model = users
        fields = ['username', 'password', 'email', 'gen', 'country']

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("Username")
        password = cleaned_data.get("Password")
        email = cleaned_data.get("Email")
        gender = cleaned_data.get("Gender")
        country = cleaned_data.get("Country")

        # Add your custom validation checks here
