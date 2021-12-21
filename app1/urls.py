from django.contrib import admin
from django.urls import path
from app1 import views
urlpatterns = [
    path('',views.index,name="index"),
    path('about',views.about,name="about"),
    path('diabetes_form',views.diabetes_form,name="diabetes_form"),
    path('diabetes_result',views.diabetes_result,name="diabetes_result")
]