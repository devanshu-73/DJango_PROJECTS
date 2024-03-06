from django.shortcuts import render,HttpResponse
from .models import *
# Create your views here.
def home(request):
    users = Form.objects.all()
    context = {'users':users}
    if request.POST:
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        form_data = Form.objects.create(
            name = name,
            email = email,
            password =  password,
        )
        return render(request,'index.html',context)
    else:
        return render(request,'index.html',context)

# def data(request):
    # return render(request,'index.html')
