from __future__ import unicode_literals

import datetime
from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
# 

class Question(models.Model):
	#item=models.ForeignKey(Item, on_delete=models.CASCADE)
	question_text=models.CharField(max_length=200)
	publish_date=models.DateTimeField('date published', default=timezone.now())
	last_modified_date=models.DateTimeField('date modified')

	def __str__(self):
		return self.question_text
	def was_last_modified(self):
		now=timezone.now()
		return now-datetime.timedelta(days=1)<=self.last_modified_date<=now
	was_last_modified.admin_order_field='last_modified_date'
	was_last_modified.boolean=True
	was_last_modified.short_description="Modified recently?"

class Choice(models.Model):
	question=models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text=models.CharField(max_length=200)
	votes=models.IntegerField(default=0)

	def __str__(self):
		return self.choice_text