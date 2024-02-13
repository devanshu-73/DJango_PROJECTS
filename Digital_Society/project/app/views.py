from django.shortcuts import render,redirect,HttpResponseRedirect
from django.urls import reverse
import random
from .utils import *

# for api
from .models import *
# from .serializers import StudentSerializer
# from rest_framework.decorators import api_view
# from rest_framework.response import Response

# # Create your views here.

# @api_view(['GET','POST'])

# def studentapi(request):
#    sdata=Student.objects.all()
#    serializer=StudentSerializer(sdata)

# default url
def home(request):
   if 'email' in request.session:
      context=data(request.session['email'])   
      return render(request, 'app/index.html',context)
   
   return render(request, "app/login.html")

def login(request):
   # if the user is already logged-in
   if 'email' in request.session:
      context=data(request.session['email'])   
      return render(request, 'app/index.html',context)
   else:
      msg=None
      try:
         # getting user input from html
         print("=========>>> Login")
         user_email=request.POST.get('email')
         user_password=request.POST.get('password')
         print("=========>>>",user_email,user_password)
         
         if(user_email != None and user_password != None):
            # if the user input is correct get the user data as an object
            context=data(user_email,user_password)
            
            if not context['user'].isActive:
               print("========== first time login")
               return render(request, 'app/firstTimeLogin.html',context)
            
            # creating a session, so the app have an info that the user is logged-in or not
            request.session['email']=context['user'].email
            
            # rendering the dashboard
            print("========== render index")
            return render(request, 'app/index.html',context)
         
      except Exception as e:
         print("===========>>> Error =",e)
         msg="Invalid Input Pls Enter Again"
         
      return render(request, "app/login.html", {'msg':msg})
   
def logout(request):
   print("==============>>> logout")
   if "email" in request.session:
      # deleting the session to notifi that the user is logged out
      del request.session['email']
   return redirect(reverse('login'))

# function for fetching user data
def data(f_email,f_password=None):
   # getting all the user data
   user=User.objects.get(email=f_email)
   if f_password:
      user=User.objects.get(email=f_email, password=f_password)
      
   if user.role.casefold()=="chairman":
      chairmanORmember=Chairman.objects.get(userid=user.id)
   else:
      chairmanORmember=Member.objects.get(userid=user.id)
   
   print("==============>>>",user,chairmanORmember)
      
   # creating a context for html
   context={
            "user":user,
            "chairmanORmember":chairmanORmember,
         }
   
   return context

def firstTimeLogin(request):
   if request.POST:
      user=User.objects.get(email=request.POST.get('email'))
      print("=========>>> Email :",user)
            
      password=request.POST.get('password')
      if password is not None and password != "":
         user.password=password
         user.isActive=True
         user.save()
         w_msg="Password Changed Successfully"
         return render(request, "app/login.html",{'w_msg':w_msg})
      else:
         msg="Pls Fillup The Fields"
         return render(request, 'app/firstTimeLogin.html',{'msg':msg,"user":user})
   return redirect('login')

def profile(request):
   # to prevent non-logged in access to the profile
   if 'email' in request.session:
      context=data(request.session['email'])
      return render(request, 'app/profile.html', context)
   else:
      return redirect('login')

def change_password(request):
   # getting the current and new password
   c_password=request.POST.get("c_password")
   n_password=request.POST.get("n_password")
   print("===============>>> ",c_password,n_password)
      
   # checking if the values are empty or not
   if c_password != None and c_password!="" and n_password != None and n_password!="":
      
      # User table / user object to access all the details of that particular user
      user=User.objects.get(email=request.session['email'])
      print("=========>>>> Password :",user.password)
      
      # password checking
      print("================>>>> Password checking")
      if user.password == c_password:
         # if correct then passord changed to new password
         user.password=n_password
         user.save()
         
         print("================>>>> Password Right")
         w_msg="Password Updated Successfully"
         # making user re-loggin with new password 
         del request.session['email']
         return render(request, 'app/login.html', {'w_msg':w_msg})
      else:
         # if incorrect then loggin-out user for safeaty reasons
         print("================>>>> Password Wrong")
         msg="Invalid Current Password"
         del request.session['email']
         return render(request, 'app/login.html', {'msg':msg})
   
   return redirect(reverse('profile'))

def change_profile(request):
   if 'email' in request.session:
      user=User.objects.get(email=request.session['email'])
      
      if user.role.casefold()=="chairman":
         chairmanORmember=Chairman.objects.get(userid=user.id)
      else:
         chairmanORmember=Member.objects.get(userid=user.id)

      print("==============>>>",user,chairmanORmember)
      
      # updating the user details
      if request.POST:
         chairmanORmember.firstname=request.POST.get('firstname') or chairmanORmember.firstname
         chairmanORmember.lastname=request.POST.get('lastname')  or chairmanORmember.lastname
         chairmanORmember.contact=request.POST.get('contact') or chairmanORmember.contact
         chairmanORmember.blockno=request.POST.get('blockno') or chairmanORmember.blockno
         chairmanORmember.houseno=request.POST.get('houseno') or chairmanORmember.houseno
         chairmanORmember.pic=request.FILES.get("pic") or chairmanORmember.pic
         if user.role.casefold()=="member":
            chairmanORmember.occupation=request.POST.get('occupation') or chairmanORmember.occupation
            chairmanORmember.vehicleno=request.POST.get('vehicleno') or chairmanORmember.vehicleno
            chairmanORmember.familyno=request.POST.get('familyno') or chairmanORmember.familyno
            chairmanORmember.tenant=request.POST.get('tenant') or chairmanORmember.tenant
         chairmanORmember.save()
   
   return redirect(reverse('profile'))

def add_member(request):
   if 'email' in request.session:
      context=data(request.session['email'])
      
      if request.POST:
         # --------- password -----------
         email=request.POST.get('email')
         contact=request.POST.get('contact')
         li=["fds32","1as3df","98dsf6","asdf132","l4y6h3","j45gf","k4hg65"]
         password=random.choice(li)+email[3:8]+contact[5:9]
         print("==========>>>> Password",password)
         # ------------------------------
         
         user=User.objects.create(email=email, password=password, role="Member")
         print("===========>>> User",user)
         if user:
            member=Member.objects.create(userid=user,
                                         firstname=request.POST.get('firstname'),
                                         lastname=request.POST.get('lastname'),
                                         contact=request.POST.get('contact'),
                                         blockno=request.POST.get('blockno'),
                                         houseno=request.POST.get('houseno'),
                                         occupation=request.POST.get('occupation'),
                                         bloodgroup=request.POST.get('bloodgroup'),
                                         vehical_details=request.POST.get('vehical_details'),
                                         job_address=request.POST.get('occupation'),
                                         )
            
            print("===========>>> Member",member)
            print("===========>>> Firstname",member.firstname)
            context['msg']="Member Added Successfully"
            
            if member:
               print("=============>>> Sending Mail")
               mymailfunction("Digital Society One Time Password","mymailtemplate",email,{'email':email,'password':password,'firstname':member.firstname})
      
      return render(request, 'app/addMember.html', context)
   else:
      return redirect('login')
   
def all_member(request):
   if 'email' in request.session:
      context=data(request.session['email'])
      mall=Member.objects.all()
      context['mall']=mall
      
      return render(request, 'app/allmembers.html',context)
   else:
      return redirect('login')
   
def edit_member(request,pk):
   if 'email' in request.session:
      context=data(request.session['email'])
      member=Member.objects.get(id=pk)
      context['member']=member
      
      if request.POST:
         member.firstname=request.POST.get('firstname') or member.firstname
         member.lastname=request.POST.get('lastname')  or member.lastname
         member.contact=request.POST.get('contact') or member.contact
         member.blockno=request.POST.get('blockno') or member.blockno
         member.houseno=request.POST.get('houseno') or member.houseno
         member.occupation=request.POST.get('occupation') or member.occupation
         member.pic=request.FILES.get("pic") or member.pic
         member.save()
         return redirect('allMember')
         
      return render(request, 'app/editMember.html',context)
   else:
      return redirect('login')
   
def delete_member(request,pk):
   if 'email' in request.session:
      member=Member.objects.get(id=pk)
      member.delete()
      
      return redirect('allMember')
   else:
      return redirect('login')

def viewMember(request,k):
   if 'email' in request.session:
      context=data(request.session['email'])
      member=Member.objects.get(id=k)
      context['member']=member
      
      return render(request, 'app/viewMember.html', context)
   else:
      return redirect('login')
 
def add_notice(request):
   if 'email' in request.session:
      context=data(request.session['email'])
      
      if request.POST:
         notice=Notice.objects.create(authority=request.POST.get('authority'),
                                      notice_title=request.POST.get('notice_title'),
                                      notice_text=request.POST.get('notice_text'),
                                      name=request.POST.get('name'),
                                      designation=request.POST.get('designation'),)
         print("===========>>> Notice",notice.notice_title)
         context['msg']="Notice Added Successfully"

      return render(request, 'app/addNotice.html',context)
   else:
      return redirect('login')
   
def allNotice(request):
   if 'email' in request.session:
      context=data(request.session['email'])
      notice=Notice.objects.all()
      context['notice']=notice

      return render(request, 'app/allNotice.html',context)
   else:
      return redirect('login')
   
def viewNotice(request,k):
   if 'email' in request.session:
      context=data(request.session['email'])
      notice=Notice.objects.get(id=k)
      context['notice']=notice

      return render(request, 'app/viewNotice.html',context)
   else:
      return redirect('login')
   
def forgotpassword(request):
   if request.POST:
      try:
         # getting user data
         user=User.objects.get(email=request.POST.get('email'))
         print("==========>>>> User",user)
         
         # ---------- step-2: Verify the otp -----------
         otp=request.POST.get('otp')
         print("==========>>>> OTP",otp)
         if otp is not None:
            # on correct OTP send to changepassword html
            if otp==user.otp and otp!="":
               return render(request, 'app/changepassword.html',{'email':user.email})
            else:
            # on incorrect OTP
               msg="Incorrect OTP"
               return render(request, 'app/forgotpassword.html',{'isOTP':True,'email':user.email,'msg':msg})
         # ----------------------------------------------
         
         # --------- step-1: otp ---------------   
         # generating otp
         user.otp=random.randint(1111,9999)
         user.save()
         
         # sending otp to the user through the mail
         mymailfunction("Forgot Password",'mailtemplate',user.email,{'email':user.email,'password':user.otp})
         # on valid email the OTP field will be unlocked
         return render(request, 'app/forgotpassword.html',{'isOTP':True,'email':user.email})
         # -------------------------------------
         
      except Exception as e:
         # if email is invalid
         print("=========>>> Error :",e)
         msg="Email is not Registered"
         return render(request, 'app/forgotpassword.html',{'msg':msg})
      
   return render(request, 'app/forgotpassword.html')

# Note: user.email is given on almost every render to keep the view connected

def changepassword(request):
   if request.POST:
      # user and password
      user=User.objects.get(email=request.POST.get('email'))
      password=request.POST.get('password')
      repassword=request.POST.get('repassword')
      
      # checking passwords for any falsy values
      if password is not None and password !="" and repassword is not None and repassword !="":
         # if the password is equal to previous password
         if user.password==password:
            msg="Same as Previous Password"
            return render(request, 'app/changepassword.html',{'email':user.email,'msg':msg})
         # successfull outcome
         elif password==repassword:
            # saving the new password
            user.password=password
            user.save()
            w_msg="Password Changed Successfully"
            return render(request, 'app/login.html',{'w_msg':w_msg})
         else:
            # if the both passwords don't match
            msg="Enter Matching Passwords"
            return render(request, 'app/changepassword.html',{'email':user.email,'msg':msg})
      else:
         # if the fields are empty
         msg="Please Fillup the Password fields Properly"
         return render(request, 'app/changepassword.html',{'email':user.email,'msg':msg})

   # the only request.POST getting on default is the email. which after the OTP is verified
   # and without that the view will return login by default
   # this prevents any malicious activites from changing the password without OTP verification 
   return redirect('login')