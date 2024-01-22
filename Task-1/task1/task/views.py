# views.py
from django.shortcuts import render, HttpResponseRedirect
from .models import User_details
from django.urls import reverse
from django.http import JsonResponse

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

def update_user(request):
    if request.method == 'POST':
        user_id = request.POST.get('id')
        user = User_details.objects.get(id=id)

        context = {'user': user}
        user.save()
        return render(request, 'editpage.html', context)

    # Handle cases where the view is accessed directly without a POST or GET request
    return HttpResponseRedirect(reverse('dashboard'))
    