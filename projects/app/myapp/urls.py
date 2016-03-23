from django.conf.urls import url, include
from . import views
urlpatterns=[
	url(r'^$',views.login_user, name='login'),
	url(r'^register/$',views.register, name='register'),
]