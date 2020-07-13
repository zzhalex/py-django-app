from django.urls import path
from . import views


urlpatterns = [
    path('', views.index,name='index'),
    path('<str:category>/', views.switchType,name='switchType'),
    path('function/addnew/',views.addnew, name='addnew'),
    path('function/getData/',views.getData,name='getData'),
]
