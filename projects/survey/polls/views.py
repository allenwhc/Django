from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, Http404
from .models import Item, Question, Choice
from django.template import loader

# Create your views here.
def index(request):
	item_list=Item.objects.order_by('id')[:10]
	return render(request, 'polls/index.html', {'item_list':item_list})

def detail(request, item_id):
	item=get_object_or_404(Item, pk=item_id)
	return render(request,'polls/item.html',{'item':item})

def vote(request, item_id):
	item=get_object_or_404(Item, pk=item_id)
	return HttpResponse("Thanks for your vote on %s"%item.item_text)