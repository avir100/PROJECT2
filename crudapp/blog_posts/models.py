from django.db import models
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def bpost_validate(bpost):
	if len(bpost) < 5:
		raise ValidationError("Length of post too short (must be greater than 5)")

def name_validate(n):
	if len(n) < 3:
		raise ValidationError("Length of name too short (must be greater than 3)")


# Create your models here.
class Post(models.Model):
	first_name=models.CharField(max_length=30, validators=[name_validate])
	last_name=models.CharField(max_length=30, validators=[name_validate])
	email=models.EmailField(max_length=50)
	bpost = models.Field(validators = [bpost_validate])

	
	def __str__(self):
		return self.first_name
	class Meta:
		db_table = "post"
		verbose_name_plural = "post"

