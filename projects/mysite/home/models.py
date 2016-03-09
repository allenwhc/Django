from __future__ import unicode_literals

import datetime
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
class Question(models.Model):
	question_text=models.CharField(max_length=200)
	pub_date=models.DateTimeField('data published')
	last_modified_date=models.DateTimeField('date modified',default=timezone.now())

	def __str__(self):
	 	return self.question_text
	# def last_updated(self):
	# 	return timezone.localtime(timezone.now())
	def  was_published_recently(self):
		return self.pub_date>=timezone.now()-datetime.timedelta(days=1)

class SubQuestion(models.Model):
	question=models.ForeignKey(Question, on_delete=models.CASCADE)
	question_text=models.CharField(max_length=200)
	pub_date=models.DateTimeField('date published')
	last_modified_date=models.DateTimeField('date modified',default=timezone.now())

	def __str__(self):
		return self.question_text
	def was_published_recently(self):
		return self.pub_date>=timezone.now()-datetime.timedelta(days=1)

class Choice(models.Model):
	question=models.ForeignKey(SubQuestion, on_delete=models.CASCADE)
	choice_text=models.CharField(max_length=200)
	votes=models.IntegerField(default=0)

	def __str__(self):
		return self.choice_text

		