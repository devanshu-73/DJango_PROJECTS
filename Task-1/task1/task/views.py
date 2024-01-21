# views.py
from django.shortcuts import render, HttpResponseRedirect
from .models import User_details
from django.urls import reverse

def dashboard(request):
    if request.POST:
        u_name = request.POST['name']
        u_subjects = request.POST.getlist('subject[]')
        u_gender = request.POST['gender']
        user = User_details.objects.create(name=u_name, subjects=u_subjects, gender=u_gender)
        user_details = User_details.objects.all()
        context={
            'user_details':user_details
        }
        return render(request, 'index.html', context)
    else:
        user_details = User_details.objects.all()
        context={
            'user_details':user_details
        }
        return render(request, 'index.html', context)
    
def delete_user(request,srno):
        user_no = User_details.objects.get(id = srno)
        print("===============>",user_no)
        user_no.delete()  # delete 
        return HttpResponseRedirect(reverse("dashboard"))