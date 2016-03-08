from django.conf.urls import url
from . import views

urlpatterns=[
	url(r'^$',views.index, name='index'),
	url(r'^(?P<question_id>[0-9]+)/$',views.details, name='details'),
	url(r'^(?P<question_id>[0-9]+)/results/$',views.results, name='results'),
	url(r'^(?P<question_id>[0-9]+)/votes/$', views.votes, name='votes')
]