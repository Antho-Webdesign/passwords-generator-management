from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
import random, string
from .models import GenPass
from .forms import PassGenForm
from django.views import View
import re

User = get_user_model()

# Create your views here.

def home(request):
    if request.method != "POST":
        return render(request, 'generator/home.html')
    else:
        site = request.POST.get('site')
        if site == "":
            return render(request, 'generator/home.html')
        password_length = int(request.POST.get('length'))
        characters = "!@#$%^&**()_+"
        numbers = '1234567890'
        small_letters = "qwertyuioplkjhgfdsazxcvbnm"
        upper_case = "QWERTYUIOPASDFGHJKLMNBVCXZ"
        prep = characters + numbers + small_letters + upper_case
        if password_length > 30:
            message = "can't generate password more than 30 characters"
            context = {
                'message': message
            }
            return render(request, 'generator/home.html', context)

        else:
            passwd = ''.join(random.sample(prep, k=password_length))
            print(passwd)
            p = GenPass.objects.create(site=site, passwords=passwd, user=request.user)
            p.save()
            context = {
                'password': passwd
            }
            return render(request, 'generator/home.html', context)

def listall(request):
    results = GenPass.objects.all()
    user = request.user
    items = GenPass.objects.filter(user=user)
    context = {
        'results': results,
        'items': items,
        'user': user,
    }
    return render(request, 'generator/listalll.html',context)



def search(request):
    if request.method == "POST":
        if query := request.POST.get('site', None):
            results = GenPass.objects.filter(site__contains=query, user=request.user)
            return render(request, 'generator/search.html', {'results': results})
    return render(request, 'generator/search.html')


def deleterecord(request, id):
    obj = get_object_or_404(GenPass, id=id)
    obj.delete()
    return redirect('listall')


def home_test(request):
    return render(request, 'generator/home-test.html')

