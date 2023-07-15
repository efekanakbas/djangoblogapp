from django.shortcuts import render,HttpResponse,redirect
from .forms import registerForm,loginForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages



# Create your views here.
def register(request):
    form=registerForm(request.POST or None)
    if form.is_valid():
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        newUser=User(username=username)
        newUser.set_password(password)
        newUser.save()
        login(request,newUser)
        messages.success(request,"Başarılı bir şekilde giriş yaptınız...")

        return redirect("login")
    context={
        "form":form
    }
    return render(request,"register.html",context)  
def logoutUser(request):
    logout(request)
    messages.success(request,"Başarılı bir şekilde çıkış yaptınız...")
    return render(request,"index.html")
def loginUser(request):
    form=loginForm(request.POST or None)
    context={
        "form":form
    }
    if form.is_valid():
       username=form.cleaned_data.get("username")
       password=form.cleaned_data.get("password")
       user=authenticate(username=username,password=password)
       if user is None:
           messages.info(request,"Geçersiz kullanıcı adı veya parola!")
           return render(request,"login.html",context)
       login(request,user)
       messages.success(request,"Başarılı bir şekilde girdiniz...")
       return redirect("index")
        

    return render(request,"login.html",context)







    
