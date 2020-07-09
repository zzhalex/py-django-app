from django.urls import path
from . import views


urlpatterns = [
    path('', views.index,name='index'),
    path('addnew/',views.addnew, name='addnew'),
]
