# views.py
from django.shortcuts import render, HttpResponseRedirect
from .models import User
from django.urls import reverse

def dashboard(request):
    if request.POST:
        u_name = request.POST['name']
        u_subjects = ",".join(request.POST.getlist('subject[]'))
        # u_subjects = ",".join(request.POST.getlist('subject[]'))
        u_gender = request.POST['gender']
        user = User.objects.create(name=u_name, subject=u_subjects, gender=u_gender)

    return render(request, 'index.html')
