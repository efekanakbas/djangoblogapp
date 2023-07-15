from . import views
from django.urls import path
from django.contrib import admin
app_name="article"

urlpatterns = [
    path("addarticle/", views.addarticle,name="addarticle"),
    path("dashboard/", views.dashboard,name="dashboard"),
    path("", views.articles,name="articles"),
    path("edit/<int:id>/",views.edit,name="edit"),
    path("delete/<int:id>/",views.delete,name="delete"),
    path("detail/<int:id>/",views.detail,name="detail"),
    path("comments/<int:id>/",views.addComments,name="comments"),
   
    
    
    
    
]