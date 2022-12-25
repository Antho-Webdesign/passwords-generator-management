from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')

    return render(request, 'users/login.html')


def register(request):
    user = request.user

    if request.method == "POST":
        # traiter le formulaire
        username = request.POST.get("username")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")
        email = request.POST.get("email")
        if password == password2:
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
            profile = Profile.objects.create_profile(user=user)
            profile.save()
            return redirect('login')
        else:
            messages.info(request, 'Password not matching...')
            return redirect('register')
    else:
        # afficher le formulaire
        return render(request, 'users/register.html')
    return render(request, 'users/register.html')


@login_required
def profile(request):
    user = request.user
    profile = get_object_or_404(Profile, user=user)
    context = {
        'profile': profile
    }
    return render(request, 'users/profile.html', context)


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
