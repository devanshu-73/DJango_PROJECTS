"""
URL configuration for Ola_Clone_Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views 
urlpatterns = [
    path('', views.home, name='home'),
    path('s1-pro/', views.s1_pro, name='s1-pro'),
    path('s1-new/', views.s1_new, name='s1-new'),
    path('s1-air/', views.s1_air, name='s1-air'),
]
