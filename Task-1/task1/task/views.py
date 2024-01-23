# views.py
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
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
    user_details = User_details.objects.all()
    context={
        'user_details':user_details
    }
    return render(request, 'index.html',context)

def delete_user(request,srno):
    user_no = User_details.objects.get(id = srno).delete()  # delete 
    print("===============>",user_no)
    user_details = User_details.objects.all()
    context={
        'user_details':user_details
    }
    return HttpResponseRedirect(reverse("dashboard"), context)

def update_user(request, srno):
    user = get_object_or_404(User_details, id=srno)    
    context = {'user': user}
    return render(request, '', context)
                                                    # print("====user", user.id)
                                                    # print("====user", user.name)
                                                    # print("====user", user.subjects)
