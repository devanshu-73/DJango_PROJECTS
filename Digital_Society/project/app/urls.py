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
