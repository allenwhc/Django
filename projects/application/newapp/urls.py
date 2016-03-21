from django.conf.urls import url

from . import views
app_name='newapp'
urlpatterns=[
	url(r'^$',views.index,name='index'),
	url(r'^(?P<info_username>\w+)/$',views.info,name='info'),
]