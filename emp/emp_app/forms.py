from django import forms
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
        widgets = {
            'date_of_birth': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        }

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class UserProfileEditForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
        widgets = {
            'date_of_birth': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        }


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, label='Username')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
