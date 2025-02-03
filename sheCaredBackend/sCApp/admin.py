from django.contrib import admin
from .models import CustomUser, GynecologistProfile, PatientProfile

admin.site.register(CustomUser)
admin.site.register(GynecologistProfile)
admin.site.register(PatientProfile)
