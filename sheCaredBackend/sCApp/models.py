from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('gynecologist', 'Gynecologist'),
        ('patient', 'Patient'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='patient')
    groups = models.ManyToManyField(
        Group,
        related_name="customuser_groups",  # Change this to avoid conflicts
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_permissions",  # Change this to avoid conflicts
        blank=True
    )

    def __str__(self):
        return self.username

class GynecologistProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    specialization = models.CharField(max_length=255)
    clinic_address = models.TextField()
    experience = models.IntegerField()

    def __str__(self):
        return self.user.username

class PatientProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    age = models.IntegerField()
    medical_history = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username
