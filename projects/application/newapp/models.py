from __future__ import unicode_literals

import datetime
from django import forms
from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
	username=models.CharField(max_length=200)
	password=models.CharField(max_length=200)
	user_create_date=models.DateTimeField('date created', default=timezone.now())
	user_last_login_date=models.DateTimeField('date last login')

	def __str__(self):
		return self.username

class Information(models.Model):
	user=models.ForeignKey(User, related_name='+')
	first_name=models.CharField(max_length=200)
	middle_name=models.CharField(max_length=200)
	last_name=models.CharField(max_length=200)
	email_address=models.CharField(max_length=200)
	birth_date=models.DateField('birthday', default=None)

