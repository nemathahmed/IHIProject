from django.contrib import admin

from .models import User, Provider, Patient

admin.site.register(User)
admin.site.register(Provider)
admin.site.register(Patient)