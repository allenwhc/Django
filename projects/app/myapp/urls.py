from django.conf.urls import url, include
from . import views
urlpatterns=[
	url(r'^login/$', views.log_in, name='login'),
	url(r'^invalid/$', views.invalid, name='invalid'),
	url(r'^logout/$',views.log_out, name='logout'),
	url(r'^auth/$',views.auth,name='auth'),
	url(r'^profile/(?P<username>\w+)/$', views.profile, name='profile'),
	url(r'^register/$',views.register_user, name='register_user'),
	url(r'^register_success/$',views.register_success, name='register_success'),
]