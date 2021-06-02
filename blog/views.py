from django.shortcuts import render
from .models import *


def index (Request):
    return render (Request,"blog/index.html")
# Create your views here.

