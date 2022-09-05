from django import forms
'''
from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .forms import LoginForm, SignupForm

User = get_user_model()


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Your account has been created! You are now able to log in')

            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/signup.html', {'form': form})


# logout_user
def logout_user(request):
    logout(request)

    return redirect('index')


def signup(request):
    if request.method == "POST":
        # traiter le formulaire
        username = request.POST.get("username")
        password = request.POST.get("password")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        phone = request.POST.get("phone")
        rue = request.POST.get("rue")
        zip = request.POST.get("zip")
        ville = request.POST.get("ville")

        user = User.objects.create_user(username=username, password=password,
                                        first_name=first_name, last_name=last_name,
                                        phone=phone, rue=rue,
                                        zip=zip, ville=ville)

        login(request, user)

        return redirect('home')

    return render(request, 'accounts/signup.html')


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {'u_form': u_form, 'p_form': p_form}
    return render(request, 'users/profile.html', context)

'''
'''
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        username = request.POST.get("username")
        password = request.POST.get("password")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        phone = request.POST.get("phone")
        rue = request.POST.get("rue")
        zip = request.POST.get("zip")
        ville = request.POST.get("ville")
        user = User.objects.create_user(username=username, password=password,
                                               first_name=first_name, last_name=last_name,
                                               phone=phone, rue=rue,
                                               zip=zip, ville=ville
                                               )
                                             
        # create a form instance and populate it with data from the request:
        # check whether it's valid:
        if form.is_valid():
            return redirect('home')

        else:
            form = SignupForm()
        return render(request, 'accounts/signup.html', {'form': form})
'''

'''
def login_user(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form})



if form.is_valid():
    subject = form.cleaned_data['subject']
    message = form.cleaned_data['message']
    sender = form.cleaned_data['sender']
    cc_myself = form.cleaned_data['cc_myself']

    recipients = ['info@example.com']
    if cc_myself:
        recipients.append(sender)

    send_mail(subject, message, sender, recipients)
    return request render(request, 'index.html')

'''
