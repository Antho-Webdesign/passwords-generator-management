from django.contrib import messages
from django.contrib.auth import get_user_model, logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile

User = get_user_model()

def login_user(request):
    if request.method == "POST":
        # traiter le formulaire
        username = request.POST.get("username")
        password = request.POST.get("password")

        if user := authenticate(request, username=username, password=password):
            login(request, user)
            return redirect('home')

    return render(request, 'users/login.html')

def logout_user(request):
    logout(request)
    return redirect('home')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Votre compte a été créé! Vous pouvez maintenant vous connecter')

            user = User.objects.create_user(username=username)
            login(request, user)

            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    user = request.user
    profile = get_object_or_404(Profile, user=user)
    return render(request, 'users/profile.html', {'profile': profile})

@login_required
def updt_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Votre compte a été mis à jour !')

            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {'u_form': u_form, 'p_form': p_form}

    return render(request, 'users/updt-profile.html', context)
