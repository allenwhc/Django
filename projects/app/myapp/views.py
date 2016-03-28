from django.shortcuts import render_to_response, render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth import login,logout,authenticate
from django.core.context_processors import csrf
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def log_in(request):
	c={}
	c.update(csrf(request))
	return render(request,'login.html',c)

def invalid(request):
	return render_to_response('invalid.html',{})

def profile(request, username):
	user=get_object_or_404(User,username=username)
	return render_to_response('profile.html',{'full_name':request.user.username})

def log_out(request):
	logout(request)
	return render_to_response('logout.html',{})

def auth(request):
	username=request.POST.get('username', False)
	password=request.POST.get('password', False)
	user=authenticate(username=username,password=password)

	# Check if user is valid
	if user is not None:
		if user.is_active:
			login(request,user)
			user_name=get_object_or_404(User, username=request.user.username)
			return HttpResponseRedirect(reverse('profile',args=(user_name.username,)))
		else:
			return render(request, 'auth.html',
				{'inactive_message':'This user is no longer active!',
				 'invalid_message':None})
	else:
		return render(request,'auth.html',{'inactive_message': None,
				 'invalid_message':'Invalid username or password!'})

def register_user(request):
	if request.method=='POST':
		form=UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/register_success/')

	args={}
	args.update(csrf(request))
	args['form']=UserCreationForm

	return render_to_response('register.html',args)

def register_success(request):
	pass
