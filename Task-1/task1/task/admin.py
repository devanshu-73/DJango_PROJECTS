from django.contrib import admin
from .models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ('name','subjects','gender')

# Register your models here.
admin.site.register(User_details,UserAdmin)