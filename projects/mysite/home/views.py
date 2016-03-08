from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Question, Choice

# Create your views here.
def index(request):
	latest_question_list=Question.objects.order_by('-last_modified_date')[:10]
	template=loader.get_template('home/index.html')
	context={
		'latest_question_list':latest_question_list
	}
	return HttpResponse(template.render(context,request))

def details(request, question_id):
	return HttpResponse("Question %s " % question_id)

def results(request, question_id):
	response="You're looking at the results of question %s"
	return HttpResponse(response%question_id)

def votes(request, question_id):
	return HttpResponse("You're voting on questions %s" % question_id)
