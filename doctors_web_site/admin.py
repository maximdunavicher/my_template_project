from django.contrib import admin
from .models import UserProfile, Appointment, Doctor, AppointmentPrice

admin.site.register(UserProfile)
admin.site.register(Appointment)
admin.site.register(Doctor)
admin.site.register(AppointmentPrice)
