#-*- coding:utf-8 -*-

from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
	class Meta:
		model=User
		fields=('email','username','password')

class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)