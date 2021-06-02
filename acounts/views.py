from django.shortcuts import render

# Create your views here.
from . import models

def login(request):
    return render(request,'acounts/login.html')