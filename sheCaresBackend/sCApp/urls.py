# from django.urls import path
# from .views import (
#     signup_view,
#     login_view,
#     patient_appointments,
#     book_appointment,
#     doctor_appointments,
#     approve_appointment,
#     reject_appointment,
#     update_availability,
# )

# urlpatterns = [
#     path('signup/', signup_view, name='signup'),
#     path('login/', login_view, name='login'),
#     path('patient/appointments/', patient_appointments, name='patient_appointments'),
#     path('patient/book_appointment/<int:doctor_id>/', book_appointment, name='book_appointment'),
#     path('doctor/appointments/', doctor_appointments, name='doctor_appointments'),
#     path('doctor/approve_appointment/<int:appointment_id>/', approve_appointment, name='approve_appointment'),
#     path('doctor/reject_appointment/<int:appointment_id>/', reject_appointment, name='reject_appointment'),
#     path('doctor/update_availability/', update_availability, name='update_availability'),
# ]
from django.urls import path
from .views import login_view, signup_view

urlpatterns = [
    path('api/login/', login_view, name='api-login'),
    path('api/signup/', signup_view, name='api-signup'),
]
