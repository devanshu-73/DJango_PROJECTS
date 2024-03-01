from django.contrib import admin
from .models import Appointment
from .models import Doctor
from .models import Customer
from .models import Moderator
from .models import User


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('start_time', 'end_time', 'date', 'doctor', 'has_not_customer', 'is_outdated',
                    'is_working_day_appointment')

    list_filter = ['start_time', 'date']

    search_fields = ['start_time', 'date']


class DoctorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'specialization')
    list_filter = ['specialization']
    search_fields = ['first_name', 'last_name']


# class UserAdmin(admin.ModelAdmin):
#     list_display = ('username', 'first_name', 'last_name')


admin.site.register(Moderator)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Customer)
admin.site.register(Appointment, AppointmentAdmin)
# admin.site.register(User, UserAdmin)

