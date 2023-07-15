from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .forms import articlesForm
from article.models import Article,Comment
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse






# Create your views here.
@login_required(login_url="user:login")
def dashboard(request):
    articles=Article.objects.filter(author=request.user)
    context={
        "articles":articles
    }
    return render(request,"dashboard.html",context)
def articles(request):
    keyword=request.GET.get("keyword")
    if keyword:
        articles=Article.objects.filter(title__contains=keyword)
        return render(request,"articles.html",{"articles":articles})
    else:
        articles=Article.objects.all()
        context={
        "articles":articles,
        
        }

        return render(request,"articles.html",context)
@login_required(login_url="user:login")
def addarticle(request):
    form=articlesForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        NewArticle=form.save(commit=False)
        NewArticle.author=request.user
        NewArticle.save()
        messages.success(request,"Başarılı bir şekilde makale kaydettiniz...")
        return redirect("article:dashboard")
    context={
        "form":form
    }
    return render(request,"addarticle.html",context)
@login_required(login_url="user:login")
def edit(request,id):
    article=get_object_or_404(Article,id=id)
    form=articlesForm(request.POST or None,request.FILES or None,instance=article)
    if form.is_valid():
        article=form.save(commit=False)
        article.author=request.user
        article.save()
        messages.success(request,"Başarılı bir şekilde makale güncellediniz...")
        return redirect("article:dashboard")
    return render(request,"edit.html",{"form":form})
@login_required(login_url="user:login") 
def delete(request,id):
    article=get_object_or_404(Article,id=id)
    article.delete()
    messages.success(request,"Başarıyla silindi...")
    return redirect("article:dashboard")
@login_required(login_url="user:login")
def detail(request,id):
    article=get_object_or_404(Article,id=id)
    comments=article.comments.all()
    content={
        "article":article,
        "comments":comments,
    }
    return render(request,"detail.html",content)
def addComments(request,id):
    article=get_object_or_404(Article,id=id)
    if request.method=="POST":
        comment_author=request.POST.get("comment_author")
        comment_content=request.POST.get("comment_content")
        newComment=Comment(comment_author=comment_author,comment_content=comment_content)
        newComment.article=article
        newComment.save()
    return redirect(reverse("article:detail",kwargs={"id":id}))












    
