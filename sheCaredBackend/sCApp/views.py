from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from .models import GynecologistProfile, PatientProfile
from .serializers import UserSerializer, GynecologistProfileSerializer, PatientProfileSerializer

User = get_user_model()

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data
        user_type = data.get('user_type')

        user = User.objects.create_user(
            username=data['username'],
            email=data['email'],
            password=data['password'],
            user_type=user_type
        )

        if user_type == 'gynecologist':
            GynecologistProfile.objects.create(
                user=user,
                specialization=data['specialization'],
                clinic_address=data['clinic_address'],
                experience=data['experience']
            )
        else:
            PatientProfile.objects.create(
                user=user,
                age=data['age'],
                medical_history=data.get('medical_history', "")
            )

        return Response({"message": "User registered successfully!"})

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(username=email, password=password)

        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "user_type": user.user_type
            })
        return Response({"error": "Invalid credentials"}, status=400)
