from django.urls import path 

from . import views

customerApp=''

urlpatterns = [
    path('',views.customer_list,name='index')
]