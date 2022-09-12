from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path

from users.views import register, profile, updt_profile

urlpatterns = [
    path('register/', register, name='register'),  # Inscription
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),  # Connexion
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout'),  # Déconnection

    # Reset Password
    path('password-reset/', PasswordResetView.as_view(template_name='users/password_reset.html'),
         name='password_reset'),

    # Reset Password Validation
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),

    # Reset Password Confirmation
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),

    # Reset Password Complete
    path('password-reset-complete/', PasswordResetCompleteView.as_view(
        template_name='users/password_reset_complete.html'
    ), name='password_reset_complete'),

    # Updt_profile
    path('modifier-profile/', updt_profile, name="updt_profile")
]
