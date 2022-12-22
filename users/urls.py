from django.urls import path

from .views import register, login_user, logout_user, profile, updt_profile

urlpatterns = [
    path('register/', register, name='register'),  # Inscription
    path('logout/', logout_user, name='logout'),  # Déconnexion
    path('login/', login_user, name='login'),  # Profil
    path('profile/', profile, name='profile'),  # Profil
    path('updt_profile/', updt_profile, name='updt_profile'),  # Profil
    # Reset Password
    # path('password-reset/', PasswordResetView.as_view(template_name='users/password_reset.html'),
    #     name='password_reset'),

    # Reset Password Validation
    # path('password-reset/done/', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
    #     name='password_reset_done'),

    # Reset Password Confirmation
    # path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
    #    template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),

    # Reset Password Complete
    # path('password-reset-complete/', PasswordResetCompleteView.as_view(
    #    template_name='users/password_reset_complete.html'
    # ), name='password_reset_complete'),

    # Updt_profile
    # path('modifier-profile/', updt_profile, name="updt_profile")
]
