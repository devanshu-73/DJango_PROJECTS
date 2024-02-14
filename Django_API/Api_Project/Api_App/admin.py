from django.contrib import admin
from .models import *
class FormAdmin(admin.ModelAdmin):
    list_display = ('name','email','password','isActive','created_at')


# Register your models here.
admin.site.register(Form, FormAdmin)
    
