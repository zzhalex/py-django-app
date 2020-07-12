from django.urls import path
from . import views


urlpatterns = [
    path('', views.index,name='index'),
    path('addnew/',views.addnew, name='addnew'),
    path('getData/',views.getData,name='getData'),
    path('detail/',views.detail,name='detail')
]
