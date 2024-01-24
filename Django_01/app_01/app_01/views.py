from django.http import HttpResponse
from django.shortcuts import render

def firstPage(request):
    # return HttpResponse("<h1>Views : First Page</h1>")
    context={
        'page':"First Page"
    }
    return render(request,"first.html",context)
        
def secondPage(request):
    context={'page':"Second Page"}
    return render(request,"second.html",context)
    # return HttpResponse("<h1>Views : Second Page</h1>")

def thirdPage(request):
    context={'page':"Third Page"}
    return render(request,"third.html",context)
    # return HttpResponse("<h1>Views : Third Page</h1>")