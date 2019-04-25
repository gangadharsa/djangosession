from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def input(request):
    return render(request,'base.html')
def add(request):
    x=int(request.GET['t1'])
    y=int(request.GET['t2'])
    z=x+y
    resp=HttpResponse("<html><body bgcolor=blue><h1>values submitted successfully</h1></body></html>")
    resp.set_cookie('z',z,max_age=40)
    #help(resp.set_cookie)
    return resp
def display(request):
    for a,b in request.COOKIES.items():
        print(a,b)
    if 'z' in request.COOKIES:
        sum=request.COOKIES['z']
        return HttpResponse("<html><body bgcolor=green><h1>Addition of two number is</h1></body></html>"+sum)
    else:
        return render(request,'base.html')