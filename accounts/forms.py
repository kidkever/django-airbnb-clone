from django import forms
from django.forms import fields
from .models import Profile
from property.models import Property
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'phone_number', 'address']


class AddListingForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['name', 'image', 'price',
                  'description', 'place', 'category']
