from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Device, CustomUser, Medicamento


class RegisterForm(UserCreationForm):
    """Cadastro público — cria apenas contas de Médico."""
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = CustomUser.Role.MEDICO
        if commit:
            user.save()
        return user


class AdminUserCreateForm(UserCreationForm):
    """Cadastro pelo painel admin — permite escolher qualquer perfil."""
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


class MedicamentoForm(forms.ModelForm):
    class Meta:
        model = Medicamento
        fields = ['name', 'principio_ativo', 'dosagem', 'quantidade', 'unidade', 'validade', 'location']
        widgets = {
            'name':            forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Dipirona'}),
            'principio_ativo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Metamizol Sódico'}),
            'dosagem':         forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 500mg'}),
            'quantidade':      forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 100'}),
            'unidade':         forms.Select(attrs={'class': 'form-control'}),
            'validade':        forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'location':        forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Farmácia - Prateleira A2'}),
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