from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserSignupForm , DoctorAvailabilityForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth import authenticate, login
from .models import Doctor, Patient , User
from django.contrib.auth.decorators import login_required



def signup_view(request):
    if request.method == "POST":
        form = UserSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()  # Save the User

            # After saving user, create a doctor or patient profile
            if user.role == 'doctor':
                doctor = Doctor(user=user)
                doctor.save()
            elif user.role == 'patient':
                patient = Patient(user=user)
                patient.save()

            return redirect('login')  # Redirect to login after successful signup

    else:
        form = UserSignupForm()

    return render(request, 'signup.html', {'form': form})
@csrf_exempt
def signup_api(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")
        role = data.get("role")
        age = data.get("age") if role == "patient" else None
        doctor_id = data.get("doctor_id") if role == "doctor" else None

        if User.objects.filter(email=email).exists():
            return JsonResponse({"error": "Email already exists"}, status=400)

        user = User.objects.create_user(username=username, email=email, password=password, role=role)
        user.age = age
        user.doctor_id = doctor_id
        user.save()
        return JsonResponse({"message": "User created successfully!"}, status=201)

    return JsonResponse({"error": "Invalid request"}, status=400)

@csrf_exempt
def login_api(request):
    if request.method == "POST":
        data = json.loads(request.body)
        email = data.get("email")
        password = data.get("password")

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return JsonResponse({"error": "Invalid email or password"}, status=400)

        user = authenticate(username=user.username, password=password)
        if user:
            login(request, user)
            return JsonResponse({"message": "Login successful!", "role": user.role}, status=200)
        else:
            return JsonResponse({"error": "Invalid credentials"}, status=400)

    return JsonResponse({"error": "Invalid request"}, status=400)

def login_view(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        # Authenticate using email
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            # Redirect to respective dashboard based on role
            if user.role == 'doctor':
                return redirect('doctor_appointments')
            elif user.role == 'patient':
                return redirect('patient_appointments')
        else:
            return JsonResponse({"error": "Invalid credentials"}, status=400)

    return render(request, "login.html")

@login_required
def doctor_appointments(request):
    doctor = Doctor.objects.get(user=request.user)  # Get the doctor linked with the logged-in user
    appointments = Appointment.objects.filter(doctor=doctor)  # Get all appointments for this doctor
    return render(request, 'doctor/appointments.html', {'appointments': appointments})

@login_required
def approve_appointment(request, appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)
    if request.method == "POST":
        appointment.status = 'approved'
        appointment.save()
        return redirect('doctor_appointments')

@login_required
def reject_appointment(request, appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)
    if request.method == "POST":
        appointment.status = 'rejected'
        appointment.save()
        return redirect('doctor_appointments')

@login_required
def patient_appointments(request):
    doctors = Doctor.objects.all()  # Get all available doctors
    return render(request, 'patient/appointments.html', {'doctors': doctors})

@login_required
def book_appointment(request, doctor_id):
    doctor = Doctor.objects.get(id=doctor_id)
    if request.method == "POST":
        appointment_time = request.POST.get('appointment_time')
        patient = Patient.objects.get(user=request.user)

        # Create appointment request
        appointment = Appointment(patient=patient, doctor=doctor, appointment_time=appointment_time)
        appointment.save()
        return redirect('patient_appointments')
    return render(request, 'patient/book_appointment.html', {'doctor': doctor})

def update_availability(request):
    doctor = Doctor.objects.get(user=request.user)  # Get the doctor linked to the logged-in user
    if request.method == "POST":
        form = DoctorAvailabilityForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()  # Save updated availability
            return redirect('doctor_appointments')  # Redirect to doctor appointments page
    else:
        form = DoctorAvailabilityForm(instance=doctor)

    return render(request, 'doctor/update_availability.html', {'form': form})

