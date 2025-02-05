from django.urls import path
from .views import signup_api, login_api ,signup_view

urlpatterns = [
    # path("signup/", signup_api, name="signup_api"),
    path("signup/", signup_view, name="signup"),
    path("login/", login_api, name="login_api"),
]
