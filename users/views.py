from django.contrib import messages
from django.contrib.auth import get_user_model, logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import RegisterForm, UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile

from django.shortcuts import render
from .forms import LoginForm


def sign_in(request):

    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('home')

        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})

    elif request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            if user := authenticate(
                request, username=username, password=password
            ):
                login(request, user)
                messages.success(
                    request, f'Hi {username.title()}, welcome back!')
                return redirect('home')

        # either form not valid or user is not authenticated
        messages.error(request, 'Invalid username or password')
        return render(request, 'users/login.html', {'form': form})


def sign_out(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')


def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'users/register.html', {'form': form})

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            return _extracted_from_sign_up_9(form, request)
        else:
            return render(request, 'users/register.html', {'form': form})
    return render(request, 'users/register.html', {'form': form})


# TODO Rename this here and in `sign_up`
def _extracted_from_sign_up_9(form, request):
    user = form.save(commit=False)
    user.username = user.username.lower()
    user.save()
    messages.success(request, 'You have singed up successfully.')
    login(request, user)
    return redirect('home')
    

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
    user = request.user
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if form.is_valid():
            form.save()
            profile = Profile.objects.create(user=user)
            profile.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request,
                'Votre compte a été créé avec succès ! Vous pouvez vous connecter.',
            )
            return redirect('login')
    else:
        form = UserRegisterForm()
        context = {
            'form': form,
            'title': 'Inscription',
            'username': username,
            'email': email,
            'password': password,
            'password2': password2,
            }

    return render(request, 'users/register.html', context)



@login_required
def profile(request):
    user = request.user

    profile = get.object_or_404(Profile, user=user)
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


