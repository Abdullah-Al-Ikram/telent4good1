from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)
    role =models.CharField(max_length=50, choices=[('volunteer', 'Volunteer'), ('organization', 'Organization')])
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',  # Change this to a unique related_name
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',  # Set a unique related_name here
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
    def __str__(self):
        return self.username

class VolunteerUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    skills = models.TextField()
    portfolio_link = models.URLField(blank=True, null=True)
    experience = models.TextField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.first_name

class Organization(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    organization_name = models.CharField(max_length=50)
    description = models.TextField()
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.organization_name

