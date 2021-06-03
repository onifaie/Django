from django.shortcuts import render
from . import models
# Create your views here.
def customer_list(Request):
    return render(Request,"customer/index.html")