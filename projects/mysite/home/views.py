from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.http import HttpResponse
from django.template import loader
from .models import Question, Choice

# Create your views here.
def index(request):
	latest_question_list=Question.objects.order_by('id')[:10]
	#template=loader.get_template('home/index.html')
	context={
		'latest_question_list':latest_question_list
	}
	return render(request,'home/index.html',context)

def details(request, question_id):
	question=get_object_or_404(Question, pk=question_id)
	return render(request, 'home/details.html', {'question':question})

def results(request, question_id):
	response="You're looking at the results of question %s"
	return HttpResponse(response%question_id)

def votes(request, question_id):
	return HttpResponse("You're voting on questions %s" % question_id)
