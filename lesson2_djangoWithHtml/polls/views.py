from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    name = "Thai duong"
    age = 16
    asset = ["xe may", "o to mecs" , "nha hang chay"]
    context = {"name":name,"age":age,"asset":asset}
    return render(request,"polls/index.html",context)