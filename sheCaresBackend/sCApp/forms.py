from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User ,Appointment, Doctor


class UserSignupForm(UserCreationForm):
    role = forms.ChoiceField(choices=User.ROLE_CHOICES, required=True)
    age = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'placeholder': 'Enter age'}))
    doctor_id = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Enter doctor ID'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'role', 'age', 'doctor_id', 'password1', 'password2']

    def clean(self):
        cleaned_data = super().clean()
        role = cleaned_data.get("role")
        age = cleaned_data.get("age")
        doctor_id = cleaned_data.get("doctor_id")

        if role == "patient" and not age:
            raise forms.ValidationError("Age is required for patients.")

        if role == "doctor" and not doctor_id:
            raise forms.ValidationError("Doctor ID is required for doctors.")

        return cleaned_data

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['appointment_time']

class DoctorAvailabilityForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['available_days', 'available_times']
