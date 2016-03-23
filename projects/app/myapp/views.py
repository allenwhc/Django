from django.shortcuts import redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from myapp.forms import UserForm, UserProfileForm
from myapp.models import UserProfile

# Create your views here.
def login_user(request):
	return render_to_response('login.html',{})

def register(request):
	context=RequestContext(request)

	# Initially, registration is failed
	registered=False

	if request.method==['POST']:
		user_form=UserForm(data=request.POST)
		profile_form=UserProfileForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user=user_form.save()	# save user form date to db
			user.set_password(user.password)	#set hashed password
			user.save()	# update user
			profile=profile_form.save(commit=False) # add delays to avoid integrity conflict
			profile.user=user
			profile.save()	# update user profile
			registered=True	# now, successfully create user

		else:
			print "error!"
	else:
		user_form,profile_form=UserForm(),UserProfileForm()

	return render_to_response('register.html',{'user_form':user_form, 'profile_form':profile_form, 'registered':registered}, context)