from django.contrib import admin
from django.urls import path
from app1 import views
urlpatterns = [
    path('',views.index,name="index"),
    path('about',views.about,name="about"),
    path('form1',views.form1,name="form1")
]