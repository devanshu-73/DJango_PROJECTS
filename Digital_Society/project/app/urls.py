
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

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
    path('allNotice/', views.allNotice, name="all-notice"),
    path('viewNotice/<int:k>', views.viewNotice, name="viewNotice"),
    # =============
    path('firstTimeLogin/', views.firstTimeLogin, name="firstTimeLogin"),
    path('viewMember/<int:k>', views.viewMember, name="viewMember"),
    path('forgotpassword/', views.forgotpassword, name="forgotpassword"),
    path('changepassword/', views.changepassword, name="changepassword"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

