from django.contrib import admin
from django.urls import path, include
from Kspl import views

urlpatterns = [
    path('boy', views.Kspl,name='Kspl'),
    path('path',views.path,name='path')
]

  