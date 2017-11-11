from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.rests_list, name='rests_list'),
	url(r'^new/$', views.restaurant_new, name='restaurant_new')
]
