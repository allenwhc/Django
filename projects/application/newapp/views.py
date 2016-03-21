from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from .models import User, Information
# Create your views here.
def index(request,username):
	return render(request,'newapp/index.html',{'username':username})

def info(request,username):
	user=get_object_or_404(Information,username=username)
	return render(request,'newapp/user_info.html',{'user':user})