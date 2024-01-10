from django.shortcuts import render,HttpResponseRedirect
from .models import * 
from django.urls import reverse 
# Create your views here.

def home (request):
    if 'email' in request.session :
        uid = User.objects.get(email = request.session['email'])
        cid = Chairman.objects.get(userid = uid)
        context = {
            'uid':uid,
            'cid':cid,
        }       
        return render(request,'app/index.html',context)
    else:
        return render(request,'app/login.html')

def login (request):
    if 'email' in request.session :
        return HttpResponseRedirect(reverse('home'))
    else:
        if request.POST:
            try:
                p_email = request.POST["email"]
                print("------------------>>>>  Email :",p_email)
                p_password = request.POST["password"]
                print("------------------>>>>  Password :",p_password)
                uid = User.objects.get(email = p_email,password = p_password)
                print("------------------>>>>  Uid :",uid)
                cid = Chairman.objects.get(userid = uid)
                print("------------------>>>>  FirstName :",cid.firstname)
                print("------------------>>>>  LastName :",cid.lastname)
                
                request.session['email']=uid.email
                return HttpResponseRedirect(reverse('home'))
                # context = {
                #     'uid':uid,
                #     'cid':cid,
                # }
                # return render(request,'app/index.html',context)
                
                # return index(request) # self practice...
            except:
                msg = "Invalid Email Or Password"
                return render(request,'app/login.html',{'e_msg':msg})
                # return home(request,msg=msg)
        else:
            print("------------------>>>>  Page Loaded")
            return render(request,'app/login.html')
            
def logout(request):
    if 'email' in request.session:
        del request.session['email']
        # return render(request,'app/login.html')
        return HttpResponseRedirect(reverse('login'))
    else:
        return HttpResponseRedirect(reverse('login'))
       
        
        
        
        
        

# ------------------------------------------------
# def home (request,msg=None):
    # e_msg = {}
    # if msg:
        # e_msg = {'e_msg':msg} 
    # return render(request,'app/login.html',e_msg)

# def index(request):
#     return render(request,'app/index.html')
# ------------------------------------------------
