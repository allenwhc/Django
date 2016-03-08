from django.test import TestCase
from models import Question, Choice

# Create your tests here.
class TestQuestion:
	q=Question.objects.get(id=1)

	def test(self):
		return self.q.question_text