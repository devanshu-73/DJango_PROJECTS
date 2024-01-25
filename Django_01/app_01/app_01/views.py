from django.http import HttpResponse
from django.shortcuts import render

def firstPage(request):
    context={'page':["First Page","Second Page","Third Page"]}
    return render(request,"first.html",context)
    # return HttpResponse("<h1>Views : First Page</h1>")
        
def secondPage(request):
    context={'page':["First Page","Second Page","Third Page"]}
    return render(request,"second.html",context)
def thirdPage(request):
    context={'page':["First Page","Second Page","Third Page"]}
    return render(request,"third.html",context)