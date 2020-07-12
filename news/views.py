from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.core import serializers

from .models import Category, Post
from django import forms
from .forms import PostForm

# Create your views here.
def index(request):
	category_list = Category.objects.all()
	usedcar_list = Post.objects.filter(category = 1).values('post_title','post_price','id','pub_date')[:20]
	context = {'categorylist': category_list,
				'usedcarlist': usedcar_list}
	print(context['categorylist'])
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
			
		else:
			return render(request,'news/add.html',{
				'from':PostForm()
				})
	# print(PostForm())
	return render(request,'news/add.html',{
		'from':PostForm()
		})

def getData(request):
	print(request)
	print(request.POST)
	dataid = request.POST['id']
	obj = Post.objects.get(id = dataid)
	data = serializers.serialize("json", [obj,])

	print(data)
	return HttpResponse(data)

def detail(request):

	return render(request,'news/detail.html',{'form':'dd'})