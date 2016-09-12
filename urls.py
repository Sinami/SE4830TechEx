from django.conf.urls import url
from . import views

app_name = 'groupTracker'
urlpatterns = [
	#ex: /groupTracker
	url(r'^$', views.index, name='index'),	
	url(r'^(?P<group_id>[0-9]+)/$', views.details, name='details'),
	#url(r'^(?P<pk>\d+)/submit/$', views.submit, name='submit'),
	url(r'^submit/(?P<pk>\d+)/$', views.submit, name='submit'),
	url(r'^showAll/$', views.showAll, name='showAll'),
	url(r'^delete/$', views.delete, name='delete'),
	#url(r'^(?P<group_id>[0-9]+)/showAll/$', views.showAll, name='showAll'),
]
