from django import forms
# from django.contrib.auth.models import User
from users.models import *
# from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(forms.ModelForm):
	email = forms.EmailField(help_text='A valid email address, please.', required = True)
	password_open = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = EmployeeDetails
		fields = ['email','password_open']
