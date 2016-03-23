from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class UserProfile(models.Model):
	user=models.OneToOneField(User)
	website=models.URLField(blank=True)
	error=models.CharField(max_length=200, default="User profile doesn't exist!")

	def __str__(self):
		return self.user.username