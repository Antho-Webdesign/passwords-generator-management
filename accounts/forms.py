from django import forms
'''
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from accounts.models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


class LoginForm(forms.Form):
    username = forms.CharField(label='Pseudo', max_length=100)
    password = forms.CharField(label='Password', max_length=100)


class SignupForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='passwords', max_length=100)
    first_name = forms.CharField(label='f name', max_length=100)
    last_name = forms.CharField(label='l name', max_length=100)
    phone = forms.CharField(label='telephone', max_length=100)
    rue = forms.CharField(label='rue', max_length=100)
    zip = forms.CharField(label='zip', max_length=100)
    ville = forms.CharField(label='Ville', max_length=100)

'''
'''
class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
    '''