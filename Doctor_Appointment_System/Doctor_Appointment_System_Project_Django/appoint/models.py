from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager
import datetime


class User(AbstractUser):
    type_choices = (
        ('M', 'Moderator'),
        ('D', 'Doctor'),
        ('C', 'Customer')
    )
    user_type = models.CharField('Type', max_length=1, choices=type_choices, default='C')
    first_name = models.CharField('First name', max_length=50)
    last_name = models.CharField('Last name', max_length=50)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

    def get_absolute_url(self):
        return '/%i' % self.pk

    def get_full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    def is_customer(self):
        """Return True if User is Customer, else False"""
        return self.user_type == 'C'

    def is_doctor(self):
        """Return True if User is Doctor, else False"""
        return self.user_type == 'D'

    def is_moderator(self):
        """Return True if User is Moderator, eld False"""
        return self.user_type == 'M'


class ModeratorManager(UserManager):
    def get_queryset(self):
        return super().get_queryset().filter(user_type='M')


class DoctorManager(UserManager):
    def get_queryset(self):
        return super().get_queryset().filter(user_type='D')


class CustomerManager(UserManager):
    def get_queryset(self):
        return super().get_queryset().filter(user_type='C')


class Moderator(User):
    objects = ModeratorManager()

    class Meta:
        ordering = ['last_name']

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.user_type = 'M'
        return super().save(*args, **kwargs)

    def get_full_name(self):
        return '%s %s' % (self.first_name, self.last_name)


class Doctor(User):
    objects = DoctorManager()
    specialization = models.CharField('Specialization', max_length=50)
    info = models.TextField('Information', max_length=1250, blank=True)

    class Meta:
        ordering = ['specialization', 'last_name']

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.user_type = 'D'
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        # return f'/{self.pk}'
        return '/%i' % self.pk

    def get_full_name(self):
        return '%s %s' % (self.first_name, self.last_name)


class Customer(User):
    objects = CustomerManager()

    class Meta:
        ordering = ['last_name']

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.user_type = 'C'
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return f'/profile/{self.pk}'
        # return '/profile/%i' % self.pk

    def get_full_name(self):
        return '%s %s' % (self.first_name, self.last_name)


class Appointment(models.Model):
    start_time = models.TimeField('Start time')
    end_time = models.TimeField('End time')
    date = models.DateField('Date')
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    class Meta:
        ordering = ['start_time']

    def __str__(self):
        return str(self.start_time)

    def get_absolute_url(self):
        return f'/{self.doctor.id}/appoint/{self.id}'

    def has_not_customer(self):         # TODO: change method to opposite(has_customer instead has_not_customer)
        """
            True if this appointment has not customer.
            False if appointment already has customer.

            :return: Boolean
        """
        return self.customer is None

    def is_outdated(self):
        """
            True if this appointment is outdated.
            False if appointment is still fresh.

            :return: Boolean
        """
        today = datetime.datetime.today()
        day = datetime.datetime.combine(self.date, self.start_time)
        return day <= today

    def is_working_day_appointment(self):
        """
            True if this appointment is in working day.
            False if appointment is in weekend.

            :return: Boolean
        """
        # function helps hide appointments on weekend
        return 0 <= self.date.weekday() <= 4

    has_not_customer.boolean = True
    has_not_customer.short_description = 'Has not customer?'

    is_outdated.boolean = True
    is_outdated.short_description = 'Is Outdated?'

    is_working_day_appointment.boolean = True
    is_working_day_appointment.short_description = 'Is in working day?'
