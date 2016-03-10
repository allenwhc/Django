import datetime
from django.test import TestCase
from django.utils import timezone
from django.core.urlresolvers import reverse
from .models import Question

# Create your tests here.
def create_question(question_text, days):
	time=timezone.now()+datetime.timedelta(days=days)
	return Question.objects.create(question_text=question_text, last_modified_date=time)

class QuestionMethodTests(TestCase):

	def test_was_last_modified_old(self):
		time=timezone.now()+datetime.timedelta(days=30)
		future_question=Question(last_modified_date=time)
		self.assertEqual(future_question.was_last_modified(),False)

	def test_was_last_modified_recent(self):
		time=timezone.now()-datetime.timedelta(hours=1)
		recent_question=Question(last_modified_date=time)
		self.assertEqual(recent_question.was_last_modified(),True)

class QuestionViewTests(TestCase):

	def test_index_view_no_questions(self):
		response=self.client.get(reverse('polls:index'))
		self.assertEqual(response.status_code,200)
		self.assertContains(response, 'No polls available.')
		self.assertQuerysetEqual(response.context['question_list'],[])

	def test_index_view_with_past_question(self):
		"""
			Questions in the past should be displayed
		"""
		create_question(question_text="Past question.",days=-30)
		response=self.client.get(reverse('polls:index'))
		self.assertQuerysetEqual(response.context['question_list'],['<Question: Past question.>'])

	def test_index_view_with_future_question(self):
		"""
			Questions in the future shouldn't be displayed
		"""
		create_question(question_text="Future question.", days=30)
		response=self.client.get(reverse('polls:index'))
		self.assertContains(response,'No polls available' ,status_code=200)
		self.assertQuerysetEqual(response.context['question_list'],[])

	def test_index_view_with_past_and_future_question(self):
		"""
			If future and past question both exist, only past questions should be displayed
		"""
		create_question(question_text="Past question.",days=-30)
		create_question(question_text="Future question", days=30)
		response=self.client.get(reverse('polls:index'))
		self.assertQuerysetEqual(response.context['question_list'],['<Question: Past question.>'])

	def test_index_view_with_two_past_questions(self):
		"""
			Multiple past questions are allowed to display
		"""
		create_question(question_text="Past question 1.", days=-20)
		create_question(question_text="Past question 2.", days=-10)
		response=self.client.get(reverse('polls:index'))
		self.assertQuerysetEqual(response.context['question_list'],['<Question: Past question 2.>','<Question: Past question 1.>'])

class QuestionIndexDetailTests(TestCase):

	def test_detail_view_with_future_question(self):
		"""Question published in the future should return 404"""
		future_question=create_question(question_text="Future question.", days=30)
		response=self.client.get(reverse('polls:detail',args=(future_question.id,)))
		self.assertEqual(response.status_code,404)

	def test_detail_view_with_past_question(self):
		"""Question published in the past should return"""
		past_question=create_question(question_text="Future question.", days=-10)
		response=self.client.get(reverse('polls:detail',args=(past_question.id,)))
		self.assertContains(response,past_question.question_text,status_code=200)

		