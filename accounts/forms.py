from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, VolunteerUser, Organization


class VolunteerSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'Volunteer'
        if commit:
            user.save()
            VolunteerUser.objects.create(user=user)
        return user

class OrganizationSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'Organization'
        if commit:
            user.save()
            Organization.objects.create(user=user)
        return user