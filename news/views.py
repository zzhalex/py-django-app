from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return render(request,'news/home.html')

def addnew(request):
	return render(request,'news/add.html',{'addnew':True})

