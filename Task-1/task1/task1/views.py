from django.shortcuts import render,HttpResponseRedirect
from .models import * 
from django.urls import reverse

def dashboard(request):
    return render(request,'index.html')