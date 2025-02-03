from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import GynecologistProfile, PatientProfile

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'user_type']

class GynecologistProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = GynecologistProfile
        fields = '__all__'

class PatientProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientProfile
        fields = '__all__'
