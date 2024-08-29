from django import forms
from django.contrib.auth.models import User
from .models import *
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    confirm_password = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Password and Confirm Password do not match")

        return cleaned_data

class CustomUserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.exclude(pk=self.instance.pk).filter(username=username).exists():
            raise forms.ValidationError("A user with that username already exists.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.exclude(pk=self.instance.pk).filter(email=email).exists():
            raise forms.ValidationError("A user with that email address already exists.")
        return email


class CustomUserChangePasswordForm(forms.Form):
    old_password = forms.CharField(label='Old Password', widget=forms.PasswordInput)
    new_password = forms.CharField(label='New Password', widget=forms.PasswordInput)

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password')
        if not self.user.check_password(old_password):
            raise ValidationError("Old password is incorrect.")
        return old_password

    def clean_new_password(self):
        new_password = self.cleaned_data.get('new_password')
        if not new_password:
            raise ValidationError("This field is required.")
        return new_password

    def save(self, commit=True):
        self.user.set_password(self.cleaned_data['new_password'])
        if commit:
            self.user.save()
        return self.user

class PasswordUpdateForm(forms.ModelForm):
    password = forms.CharField(label='New Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('password',)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['full_name', 'image', 'mobile_number','address']

class CarRentForm(forms.ModelForm):
    class Meta:
        model = CarRent
        fields = [
            'name', 'model', 'color', 'topspeed', 'date_from', 'date_to','number_plate',
            'insurance', 'seats', 'price', 'image1', 'image2', 'image3', 'image4', 'image5'
        ]
        widgets = {
            'date_from': forms.DateInput(attrs={'type': 'date'}),
            'date_to': forms.DateInput(attrs={'type': 'date'}),
        }