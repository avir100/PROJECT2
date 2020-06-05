from django import forms
from django.db import models
from .models import Post
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import re



class BlogPostForm(forms.ModelForm):
	bpost = forms.CharField(widget=forms.Textarea)
	class Meta:
		model = Post
		fields = "__all__"


class RegisterForm(UserCreationForm):
	username = forms.CharField(max_length=30)
	first_name = forms.CharField(max_length=30)
	last_name = forms.CharField(max_length=30)
	email = forms.EmailField(max_length=50)
	verify_email = forms.EmailField(max_length=50)
	#password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ["username", "password1", "password2", "email", "verify_email"]

	def __str__(self):
		return self.first_name 

class LoginForm(forms.ModelForm):
	username = forms.CharField(max_length=30)
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = User
		fields = ['username', 'password']
		

	def __str__(self):
		return self.first_name 