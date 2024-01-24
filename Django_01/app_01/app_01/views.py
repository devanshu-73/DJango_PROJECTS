from django.http import HttpResponse
from django.shortcuts import render

def firstPage(request):
    # return HttpResponse("<h1>Views : First Page</h1>")
    context={
        'firstpage':"First Page"
    }
    return render(request,"first.html",context)
        
def secondPage(request):
    context={'secondpage':"Second Page"}
    return render(request,"second.html",context)
    # return HttpResponse("<h1>Views : Second Page</h1>")

def thirdPage(request):
    context={'thirdpage':"Third Page"}
    return render(request,"third.html",context)
    # return HttpResponse("<h1>Views : Third Page</h1>")