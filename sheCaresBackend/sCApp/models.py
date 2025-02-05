from django.db import models
from django.contrib.auth.models import User

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    registration_number = models.CharField(max_length=50)
    specialization = models.CharField(max_length=100)

    class Meta:
        db_table = 'doctor_table'  # Custom table name

    def __str__(self):
        return self.user.username

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()

    class Meta:
        db_table = 'patient_table'  # Custom table name

    def __str__(self):
        return self.user.username

# SELECT * FROM sCApp_user;