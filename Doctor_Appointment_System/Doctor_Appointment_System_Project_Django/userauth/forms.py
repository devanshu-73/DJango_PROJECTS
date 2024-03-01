from django.contrib.auth.forms import UserCreationForm
from appoint.models import Customer
from appoint.models import Doctor
from appoint.models import Moderator


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = Customer
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']


class RegisterDoctorUserForm(UserCreationForm):
    class Meta:
        model = Doctor
        fields = ['username', 'first_name', 'last_name', 'specialization', 'password1', 'password2']


class RegisterModeratorUserForm(UserCreationForm):
    class Meta:
        model = Moderator
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']
