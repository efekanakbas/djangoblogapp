from django.shortcuts import render,HttpResponse,redirect
def index(request): 
    return render(request,"index.html")
def about(request):
    return render(request,"about.html") 

