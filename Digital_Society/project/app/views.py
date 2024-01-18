from django.shortcuts import render,HttpResponseRedirect
from .models import * 
from django.urls import reverse
import random
from .utils import * 

"""
Django ORM 

get() : fetch data from model and return an object but only single records 
    if there are multiple records found with given condition it will thrown an exception 

"""
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
                p_password = request.POST["password"]
                uid = User.objects.get(email = p_email,password = p_password)
                cid = Chairman.objects.get(userid = uid)
                request.session['email']=uid.email
                return HttpResponseRedirect(reverse('home'))
            
                # print("------------------>>>>  Password :",p_password)
                # print("------------------>>>>  Email :",p_email)
                # print("------------------>>>>  Uid :",uid)
                # print("------------------>>>>  FirstName :",cid.firstname)
                # print("------------------>>>>  LastName :",cid.lastname)
                # return index(request) # self practice...
            except Exception as e:
                msg = "Invalid Email Or Password"
                return render(request,'app/login.html',{'e_msg':msg})
                # return home(request,msg=msg)
        else:
            # print("------------------>>>>  Page Loaded")
            return render(request,'app/login.html')
            
def logout(request):
    if 'email' in request.session:
        del request.session['email']
        return HttpResponseRedirect(reverse('login'))
    else:
        return HttpResponseRedirect(reverse('login'))

def profile(request):
    if 'email' in request.session:
        uid = User.objects.get(email = request.session['email'])
        cid = Chairman.objects.get(userid = uid)
        context = {
            'uid' : uid,
            'cid' : cid,
        }
        return render(request,'app/profile.html',context)
    else:
        return HttpResponseRedirect(reverse('login'))

 
def change_password(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        cid = Chairman.objects.get(userid = uid)
        
        currentpassword = request.POST['currentpassword']
        newpassword = request.POST['newpassword']
        if uid.password == currentpassword:
            uid.password = newpassword
            uid.save() # update 
        
            del request.session['email']
            s_msg = "Successfully Password Changed"
            return render(request,"app/login.html",{'s_msg':s_msg})
        else:
            e_msg = "Invalid current password"
            del request.session['email']
            return render(request,"app/login.html",{'e_msg':e_msg})
        
def change_profile(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        cid = Chairman.objects.get(userid = uid)
        
        if request.POST:
            cid.firstname = request.POST['firstname']
            cid.lastname =  request.POST['lastname']
            cid.contact =request.POST['contact']
            cid.houseno = request.POST['houseno']
            cid.blockno = request.POST['blockno']
            if "pic" in request.FILES:
                cid.pic = request.FILES['pic']
                cid.save()
            cid.save() # update

        context = {
                'uid' : uid,
                'cid' : cid,
        }
        return render(request,"app/profile.html",context)
       
def add_member(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        cid = Chairman.objects.get(userid = uid)

        if request.POST:
            print("---> add operation")
            email = request.POST['email']
            contact = request.POST['contact']
            firstname = request.POST['firstname']
            l1 = ["cds33frr","dsc323vs","fdv24bb","nb534vdf","mn345bgf"]
            password = random.choice(l1)+email[3:6]+contact[4:7]
            muid = User.objects.create(email = request.POST['email'],password = password,role="member") 
            if muid:
                mid = Member.objects.create(
                                userid = muid,
                                firstname = request.POST['firstname'],
                                lastname = request.POST['lastname'],
                                contact = request.POST['contact'],
                                blockno = request.POST['blockno'],
                                houseno = request.POST['houseno'],
                                occupation = request.POST['occupation'],
                                job_address = request.POST['job_address'],
                                bloodgroup = request.POST['bloodgroup'],
                                vehical_details = request.POST['vehical_details']
                        )
                if mid:
                    mymailfunction("Welcome to Digital Society","mymailtemplate",email,{'firstname' : firstname,'password':password})                    
                context = {
                    'uid' : uid,
                    'cid' : cid,
                    's_msg' : "successfully Member added"
                    }
                return render(request,"app/addMember.html",context)
                

        context = {
                'uid' : uid,
                'cid' : cid,
        }
        return render(request,"app/addMember.html",context)

        
def all_member(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        cid = Chairman.objects.get(userid = uid)
        mall = Member.objects.all()  # select * from member
        context = {
                'uid' : uid,
                'cid' : cid,
                'mall' : mall,
        }
        return render(request,"app/allmembers.html",context)
    
def edit_member(request,pk):
    if "email" in request.session:
        print("---->>>pk",pk)
        uid = User.objects.get(email = request.session['email'])
        cid = Chairman.objects.get(userid = uid)
        mid = Member.objects.get(id = pk)
        context = {
                'uid' : uid,
                'cid' : cid,
                'mid' : mid,
        }
        return render(request,"app/editMember.html",context)
    
def delete_member(request,pk):
    if "email" in request.session:
        mid = Member.objects.get(id = pk)
        mid.delete()  # delete 
        return HttpResponseRedirect(reverse("all-member"))

def add_notice(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        cid = Chairman.objects.get(userid = uid)

        if request.POST:
            notice_title = request.POST['notice_title']
            notice_description = request.POST['notice_description']
            if "pic" in request.FILES:
                pic = request.FILES['pic']
            elif "video" in request.FILES:
                video = request.FILES['video']
            elif "pic" in request.FILES and "video" in request.FILES:
                pic = request.FILES['pic']
                video = request.FILES['video']
        else:
            context = {
                'uid' : uid,
                'cid' : cid,
            }
            return render(request,"app/addNotice.html",context)
# ============================================================================================
# ============================================================================================
# ------------------------------------------------
# def home (request,msg=None):
    # e_msg = {}
    # if msg:
        # e_msg = {'e_msg':msg} 
    # return render(request,'app/login.html',e_msg)

# def index(request):
#     return render(request,'app/index.html')
# ------------------------------------------------
