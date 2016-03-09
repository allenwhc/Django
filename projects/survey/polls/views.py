from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Question, Choice

# Create your views here.
class IndexView(generic.ListView):
	template_name='polls/index.html'
	context_object_name='question_list'

	def get_queryset(self):
		return Question.objects.order_by('-publish_date')[:10]

class DetailView(generic.DetailView):
	model=Question
	template_name='polls/detail.html'


class ResultView(generic.DetailView):
	model=Question
	template_name='polls/result.html'

def vote(request, question_id):
	#item=get_object_or_404(Item, pk=item_id)
	question=get_object_or_404(Question, pk=question_id)
	try:
		selected_choice=question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'polls/detail.html',{
			'question':question,
			'error_message': "You haven't chosen yet.",
			})
	else:
		selected_choice.votes+=1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:result',args=(question.id,)))


# def test(request, question_id):
# 	item=get_object_or_404(Item, pk=item_id)
# 	question_set=Question.objects.filter(item_id=item_id)
# 	size=question_set.count
# 	return render(request, 'polls/test.html',{'question':question_set,'size':size})