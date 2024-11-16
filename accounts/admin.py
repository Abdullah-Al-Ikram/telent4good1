from django.contrib import admin

from accounts.models import User,Organization, VolunteerUser

# Register your models here.
admin.site.register(User)
admin.site.register(Organization)
admin.site.register(VolunteerUser)