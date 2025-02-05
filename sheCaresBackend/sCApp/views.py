from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserSignupForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth import authenticate, login
from .models import User


def signup_view(request):
    if request.method == "POST":
        form = UserSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            # Ensure correct fields are saved
            if user.role == "patient":
                user.doctor_id = None  # Reset doctor ID if Patient
            elif user.role == "doctor":
                user.age = None  # Reset age if Doctor

            user.save()
            return redirect("login")  # Redirect to login after signup
    else:
        form = UserSignupForm()

    return render(request, "signup.html", {"form": form})
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