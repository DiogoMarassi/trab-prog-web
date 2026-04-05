from django import forms
from .models import Device

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