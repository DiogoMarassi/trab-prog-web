from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Device, CustomUser


class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'email', 'role', 'password1', 'password2']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'email', 'role']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'role': forms.Select(attrs={'class': 'form-control'}),
        }


class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['name', 'serial_number', 'device_type', 'manufacturer', 'status', 'location']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Monitor Cardíaco'}),
            'serial_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: MC-2024-X'}),
            'device_type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Monitor'}),
            'manufacturer': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Philips'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: UTI-C Leito 03'})
        }