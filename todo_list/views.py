from django.shortcuts import render,redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect

def home(request):
	if request.method == 'POST':
		form = ListForm(request.POST or None)
		if form.is_valid():
			form.save()
			messages.success(request,('Item has been added to the list'))
			all_items = List.objects.all
			return render(request,'home.html',{'all_items' : all_items})
	else:
		all_items = List.objects.all
	# querying of db can be done in different ways.
		return render(request,'home.html',{'all_items' : all_items})
	# request is made by the webbrowser for a certain url
	# home.html is the html page which will be displayed
	# {} is a context dictionary which can be used to pass the contents to html page.

def about(request):
	name = 'Suraj'
	return render(request,'about.html',{'name' : name})

# 2 types of requests: 1 is GET and the other is POST,POST is usually made by forms and when a change needs to be made in the db

def delete(request,list_id):
	item = List.objects.get(pk=list_id)
	item.delete()
	messages.success(request,('Item has been deleted'))
	return redirect('home')
def cross_off(request,list_id):
	item = List.objects.get(pk = list_id)
	item.completed = True
	item.save()
	messages.success(request,('Item has been crossed off'))
	return redirect('home')

def uncross_off(request,list_id):
	item = List.objects.get(pk = list_id)
	item.completed = False
	item.save()
	messages.success(request,('Item has been uncrossed '))
	return redirect('home')