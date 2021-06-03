from django.urls import path 
from . import views

blogapp=''
urlpatterns = [
    path('',views.index,name='index'),

]