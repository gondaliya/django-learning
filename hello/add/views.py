from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def add(request):
    return render(request,"add.html")

def result(request):
    num1 = int(request.POST['num1'])
    num2 = int(request.POST['num2'])
    ans = num1+num2

    return render(request,'res.html',{'res':ans})