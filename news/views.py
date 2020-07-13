from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.core import serializers

from .models import Category, Post
from django import forms
from .forms import PostForm

import json
import time

# Create your views here.
def index(request):
	type = 1
	category_list = Category.objects.all()
	list = Post.objects.filter(category = type).values('post_title','post_price','id','pub_date')[:20]
	context = {'categorylist': category_list,
				'list': list}
	return render(request,'news/home.html',context)

def switchType(request,category):
	type = 1
	print(category)
	if(category=='Rentals'):
		type = 2
	category_list = Category.objects.all()
	list = Post.objects.filter(category = type).values('post_title','post_price','id','pub_date')[:20]
	context = {'categorylist': category_list,
				'list': list}
	return render(request,'news/home.html',context)

def addnew(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		print(form.data)
		if	form.is_valid():
			categoryval = form.cleaned_data['category']
			post_titleval = form.cleaned_data['post_title']
			post_textval = form.cleaned_data['post_text']
			post_priceval = form.cleaned_data['post_price']
			post_contactval = form.cleaned_data['post_contact']
			post_ownerval = form.cleaned_data['post_owner']
			# time = 
			p = Post(category=categoryval,post_text=post_textval,post_title=post_titleval,post_price=post_priceval,post_contact=post_contactval,post_owner=post_ownerval)
			p.save()
			category_list = Category.objects.all()
			list = Post.objects.filter(category = categoryval).values('post_title','post_price','id','pub_date')[:20]
			context = {'categorylist': category_list,
						'list': list}
			return render(request,'news/home.html',context)	
		else:
			return render(request,'news/add.html',{
				'from':PostForm()
				})
	# print(PostForm())
	return render(request,'news/add.html',{
		'from':PostForm()
		})

def getData(request):
	dataid = request.POST['id']
	obj = Post.objects.get(id = dataid)
	data = serializers.serialize("json", [obj,])
	return HttpResponse(data)
