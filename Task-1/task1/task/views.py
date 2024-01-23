# views.py
from django.shortcuts import render, HttpResponseRedirect,HttpResponse
from .models import User_details
from django.urls import reverse
from django.http import JsonResponse
from django.shortcuts import reverse

def dashboard(request):
    try:
        if request.POST:
            u_name = request.POST['name']
            u_subjects = request.POST.getlist('subject[]')
            u_gender = request.POST['gender']
            if not u_name or (not u_subjects and not u_gender) or (not u_subjects and not u_name) or (not u_gender and not u_name):
                script = """
                    <script>
                        alert("Please enter all details.");
                        window.location.href = "{0}";
                    </script>
                """.format(reverse("dashboard"))
                response_content = f"{script}"
                return HttpResponse(response_content)

            user = User_details.objects.create(name=u_name, subjects=u_subjects, gender=u_gender)
            user_details = User_details.objects.all()
            context = {
                'user_details': user_details
            }
            return render(request, 'index.html', context)

        user_details = User_details.objects.all()
        context = {
            'user_details': user_details
        }
        return render(request, 'index.html', context)
    except:
        return HttpResponseRedirect(reverse("dashboard"))

def delete_user(request,srno):
    user_no = User_details.objects.get(id = srno).delete()  # delete 
    print("===============>",user_no)
    user_details = User_details.objects.all()
    context={
        'user_details':user_details
    }
    return HttpResponseRedirect(reverse("dashboard"), context)

def update_user(request, srno):
    user = User_details.objects.get(id=srno)

    if request.method == 'POST':
        user.name = request.POST.get('name')
        user.gender = request.POST.get('gender')
        if 'subject[]' in request.POST:
            user.subjects = request.POST.getlist('subject[]')
        else:
            user.subjects = []
        user.save()
        return HttpResponseRedirect(reverse('dashboard'))

    context = {'user': user, 'subs': ['c', 'c++', 'python', 'js']}
    return render(request, 'editpage.html', context)
