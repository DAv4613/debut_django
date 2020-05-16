from django import forms
from django.contrib.auth.models import User

from django.contrib.auth.models import User 
from django.core.validators import validate_email



class UserForm(forms.ModelForm):
	username = forms.CharField(widget=forms.TextInput( 
		attrs= {'class':'form-control', 'placeholder': 'username'}), required=True, max_length=50)
	email = forms.CharField(widget=forms.EmailInput( 
		attrs= {'class':'form-control', 'placeholder': 'email'}), required=True, max_length=50)
	first_name = forms.CharField(widget=forms.TextInput( 
		attrs= {'class':'form-control', 'placeholder': 'first_name'}), required=True, max_length=50)
	last_name = forms.CharField(widget=forms.TextInput( 
		attrs= {'class':'form-control', 'placeholder': 'last_name'}), required=True, max_length=50)
	password = forms.CharField(widget=forms.PasswordInput( 
		attrs= {'class':'form-control', 'placeholder': 'username'}), required=True, max_length=50)
	confirm_password = forms.CharField(widget=forms.PasswordInput( 
		attrs= {'class':'form-control', 'placeholder': 'username'}), required=True, max_length=50)


	class Meta():
		model = User
		fields = ['username','email','first_name','last_name','password']


	def clean_username(self):
		user = self.cleaned_data['username']
		try:
			match = User.objects.get(username=user)
		except:
			return self.cleaned_data['username']
		raise forms.ValidationError("ce nom existe")

	def clean_email(self):
		email = self.cleaned_data['email']
		try:
			my = validate_email(email)
		except:
			return forms.ValidationError("email incorrect")
		return email 

	def clean_confirm_password(self):
		pas = self.cleaned_data['password']
		cpas = self.cleaned_data['confirm_password']
		MIN_LENGTH = 8
		if pas and cpas:
			if pas != cpas:
				raise forms.ValidationError("mot de passe different")
			else:
				if len(pas) < MIN_LENGTH:
					raise forms.ValidationError("password should have atleast %d characters"%MIN_LENGTH)
				if pas.isdigit():
					raise forms.ValidationError("Password should not all numeric")
