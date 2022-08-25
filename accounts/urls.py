from django.urls import path
from .views import (
    RegisterUserView,
    ActivateUserView,
    UserLoginView,
    ForgotPasswordView,
    PasswordResetValidateView,
    PasswordResetView,
    logout)

app_name = "accounts"
urlpatterns = [
    path("register", RegisterUserView.as_view(), name="register"),
    path("login", UserLoginView.as_view(), name="login"),
    path("logout", logout, name="logout"),

    path("activate/<uidb64>/<token>/", ActivateUserView.as_view(), name="activate"),
    path("forgotPassword/", ForgotPasswordView.as_view(), name="forgotPassword"),
    path("resetpassword_validate/<uidb64>/<token>/", PasswordResetValidateView.as_view(), name="resetpassword_validate"),
    path("resetPassword/", PasswordResetView.as_view(), name="resetPassword"),
]
