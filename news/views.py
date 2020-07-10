from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Post
from .forms import PostForm
# Create your views here.
def index(request):
	category_list = Category.objects.all()
	context = {'categorylist': category_list}
	print(context['categorylist'])
	return render(request,'news/home.html',context)

def addnew(request):
	return render(request,'news/add.html',{'addnew':True})

