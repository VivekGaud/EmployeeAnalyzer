from django import forms
from users.models import *
from csvReader.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# class UserRegisterForm(UserCreationForm):
#     email = forms.EmailField()

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']
def get_primary_category():
	primary_category_opt = ProcessCategory.objects.all().only("pk","name")
	primary_category = []

	for a_primary_category_opt in primary_category_opt:
		temp_primary_category_obj = []
		temp_primary_category_obj.append(a_primary_category_opt.pk)
		temp_primary_category_obj.append(a_primary_category_opt.name)
		primary_category.append(temp_primary_category_obj)

	return primary_category

class EmployeeDetailsForm(forms.ModelForm):
	# def __init__(self):
	email = forms.EmailField(help_text='A valid email address, please.', required = True)
	password_open = forms.CharField(label = "Password",widget=forms.PasswordInput())
	primary_category = get_primary_category()

	primary_category = forms.ChoiceField(choices=primary_category)

	class Meta:
		model = EmployeeDetails
		fields = ('email', 'password_open','primary_category')

class CategoryDifferenceReasonForm(forms.ModelForm):
	# difference_reason = forms.CharField(required = True)

	class Meta:
		model = LoginInstances
		fields = ('difference_reason',)

class EmployeeRegForm(forms.ModelForm):
	email = forms.EmailField(help_text='A valid email address, please.', required = True)
	password_open = forms.CharField(label = "Password", widget=forms.PasswordInput())

	class Meta:
		model = EmployeeDetails
		fields = ('email', 'password_open')

class EmployeeRegisterForm(forms.ModelForm):
	email = forms.EmailField(help_text='A valid email address, please.', required = True)
	password_open = forms.CharField(label = "password", widget=forms.PasswordInput())
	password_confirm=forms.CharField(label="password_confirm", widget=forms.PasswordInput())
	class Meta:
		model = EmployeeRegister
		fields = ('email', 'password_open','password_confirm')
