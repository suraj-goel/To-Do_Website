from django.urls import path
from . import views
urlpatterns = [
	path('',views.home, name = 'home'),
	# localhost/ redirected to home method in views.py
	# name is used to refer to the above url by just using home var.
	path('about/',views.about, name='about'),
	path('delete/<list_id>',views.delete,name = 'delete'),
	path('cross_off/<list_id>',views.cross_off,name = 'cross_off'),
	path('uncross_off/<list_id>',views.uncross_off,name = 'uncross_off'),
]
