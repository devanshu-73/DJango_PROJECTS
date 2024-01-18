"""
URL configuration for project project.

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
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
    path('profile/',views.profile,name="profile"),
    path('change-password/',views.change_password,name="change-password"),
    path('change-profile/',views.change_profile,name="change-profile"),
    path('add-member/',views.add_member,name="add-member"),
    path('all-member/',views.all_member,name="all-member"),
    path('edit-member/<int:pk>',views.edit_member,name="edit-member"),
    path('delete-member/<int:pk>',views.delete_member,name="delete-member"),
    path('add-notice/',views.add_notice,name="add-notice"),
]
