from django.http import HttpResponse
from django.shortcuts import render

def firstPage(request):
    # return HttpResponse("<h1>Views : First Page</h1>")
    return render(request,"first.html")
    
    
def secondPage(request):
    return render(request,"second.html")
    # return HttpResponse("<h1>Views : Second Page</h1>")


def thirdPage(request):
    return render(request,"third.html")
    # return HttpResponse("<h1>Views : Third Page</h1>")