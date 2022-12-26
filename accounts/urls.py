from django.urls import path

from .views import SignUpView, MyProfile, MyLoginView, login_user, logout_user

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="register"),
    path('profile/', MyProfile.as_view(),name='profile'),
    path('profile/update/', MyProfile.as_view(),name='profile_update'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]
