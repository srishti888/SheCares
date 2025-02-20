from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

class User(AbstractUser):
    # Define role choices
    ROLE_CHOICES = (
        ('doctor', 'Doctor'),
        ('patient', 'Patient'),
    )
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    age = models.IntegerField(null=True, blank=True)  # Only for Patients
    doctor_id = models.CharField(max_length=20, null=True, blank=True)  # Only for Doctors
    # Define related_name for groups and permissions to avoid clashes
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='sCApp_user_groups',  # Custom related_name
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='sCApp_user_permissions',  # Custom related_name
        blank=True,
    )
    def __str__(self):
        return self.username
# Doctor Model
class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Linking to the User model (Doctor)
    name = models.CharField(max_length=100 , default="xyz")
    registration_number = models.CharField(max_length=100 , default="xyz")
    specialization = models.CharField(max_length=100 ,default="xyz" )
    available_days = models.CharField(max_length=100 , default="Monday")  # E.g., "Mon, Tue, Wed"
    available_times = models.TextField(default="xyz")  # Store timeslots as text, or you can normalize with another model

    def __str__(self):
        return self.name


# Patient Model
class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Linking to the User model (Patient)
    name = models.CharField(max_length=100 , default="xyz")
    email = models.EmailField(unique=True , default="123@gmail.com")
    phone_number = models.CharField(max_length=15 , default="xyz")

    def __str__(self):
        return self.name


# Appointment Model
class Appointment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_time = models.DateTimeField()  # The time the patient wants to book
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Appointment with {self.doctor.name} at {self.appointment_time}"
