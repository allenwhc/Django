from __future__ import unicode_literals

import datetime
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
class Item(models.Model):
	item_text=models.CharField(max_length=200)
	publish_date=models.DateTimeField('date published', default=timezone.now())
	last_modified_date=models.DateTimeField('date modified')

	def __str__(self):
		return self.item_text
	def is_last_published(self):
		return self.publish_date>=timezone.now()-datetime.timedelta(days=1)

class Question(models.Model):
	item=models.ForeignKey(Item, on_delete=models.CASCADE)
	question_text=models.CharField(max_length=200)
	publish_date=models.DateTimeField('date published', default=timezone.now())
	last_modified_date=models.DateTimeField('date modified')

	def __str__(self):
		return self.item_text
	def is_last_published(self):
		return self.publish_date>=timezone.now()-datetime.timedelta(days=1)

class Choice(models.Model):
	question=models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text=models.CharField(max_length=200)
	votes=models.IntegerField(default=0)

	def __str__(self):
		return self.choice_text