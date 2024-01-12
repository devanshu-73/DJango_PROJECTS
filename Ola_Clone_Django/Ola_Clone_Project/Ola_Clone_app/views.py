from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')
def s1_pro(request):
    return render(request,'s1-pro.html')

def s1_new(request):
    return render(request,'s1-new.html')

def s1_air(request):
    return render(request,'s1-air.html')