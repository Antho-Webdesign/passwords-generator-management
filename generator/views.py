from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
import random
from .models import GenPass

User = get_user_model()

# Create your views here.

def home(request):
    if request.method == "POST":
        site = request.POST.get('site')
        user = request.POST.get('user.username')
        if site == "":
            return render(request, 'generator/home.html')
        password_length = int(request.POST.get('length'))
        if password_length > 30:
            message = "can't generate password more than 30 characters"
            context = {'message': message}
            return render(request, 'generator/home.html', context)
        else:
            user = request.user
            numbers = '1234567890'
            small_letters = "qwertyuioplkjhgfdsazxcvbnm"
            prep = f"!@#$%^&**()_+{numbers}{small_letters}QWERTYUIOPASDFGHJKLMNBVCXZ"
            passwd = ''.join(random.sample(prep, k=password_length))
            print(passwd)
            p = GenPass.objects.create(site=site, passwords=passwd, user=user)

            p.save()
            context = {
                'password': passwd,
                'site': site,
                'user': user,
            }
            return render(request, 'generator/success.html', context)
    return render(request, "generator/home.html")


@login_required
def listall(request):
    user = request.user
    items = GenPass.objects.filter(user=user)
    results = GenPass.objects.filter(user=user)
    context = {
        'results': results,
        'items': items,
        'user': user,
    }
    return render(request, 'generator/listalll.html', context)


def search(request):
    if request.method == "POST":
        if query := request.POST.get('site', None):
            results = GenPass.objects.filter(site__contains=query)
            return render(request, 'generator/search.html', {'results': results})
    return render(request, 'generator/search.html')


def deleterecord(request, id):
    obj = get_object_or_404(GenPass, id=id)
    obj.delete()
    return redirect('listall')


def home_test(request):
    return render(request, 'generator/home-test.html')

