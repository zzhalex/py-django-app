from django.shortcuts import render
from django.http import HttpResponse
<<<<<<< HEAD
from .models import Category, Post
from .forms import PostForm
# Create your views here.
def index(request):
	category_list = Category.objects.all()
	context = {'categorylist': category_list}
	print(context['categorylist'])
	return render(request,'news/home.html',context)
=======

# Create your views here.
def index(request):
	return render(request,'news/home.html')
>>>>>>> c83d230948e5225f752cf55d34ff15e2b2765ece

def addnew(request):
	return render(request,'news/add.html',{'addnew':True})

