from django.contrib import admin
from .models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ('srno','name','subject','gender')

# Register your models here.
admin.site.register(User,UserAdmin)