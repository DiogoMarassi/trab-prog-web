from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Device, CustomUser, Medicamento
from .forms import DeviceForm, MedicamentoForm, RegisterForm, UserEditForm, AdminUserCreateForm


class EngenheiroRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and (
            self.request.user.role == 'ENGENHEIRO' or self.request.user.is_superuser
        )

    def handle_no_permission(self):
        return render(self.request, '403.html', status=403)


class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)

        if user is None:
            return render(request, 'login.html', {'form_errors': True})

        # Gera par de tokens JWT
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        response = redirect('home')

        # Armazena tokens em cookies httpOnly (JavaScript não consegue ler)
        response.set_cookie(
            'access_token', access_token,
            httponly=True, samesite='Lax'
        )
        response.set_cookie(
            'refresh_token', refresh_token,
            httponly=True, samesite='Lax'
        )
        return response


class RegisterView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, 'register.html', {'form': form})


class LogoutView(View):
    def post(self, request):
        response = redirect('login')
        response.delete_cookie('access_token')
        response.delete_cookie('refresh_token')
        return response


@login_required
def home(request):
    return redirect('devices')


@login_required
def devices_panel(request):
    devices = Device.objects.all()
    medicamentos = Medicamento.objects.all()
    return render(request, 'devices.html', {'devices': devices, 'medicamentos': medicamentos})


@login_required
def users_panel(request):
    if not (request.user.role == 'ENGENHEIRO' or request.user.is_superuser):
        return render(request, '403.html', status=403)
    users = CustomUser.objects.all().order_by('username')
    return render(request, 'users.html', {'users': users})


class MedicamentoCreateView(LoginRequiredMixin, EngenheiroRequiredMixin, CreateView):
    model = Medicamento
    form_class = MedicamentoForm
    template_name = 'medicamento_form.html'
    success_url = reverse_lazy('devices')


class MedicamentoUpdateView(LoginRequiredMixin, EngenheiroRequiredMixin, UpdateView):
    model = Medicamento
    form_class = MedicamentoForm
    template_name = 'medicamento_form.html'
    success_url = reverse_lazy('devices')


class MedicamentoDeleteView(LoginRequiredMixin, EngenheiroRequiredMixin, DeleteView):
    model = Medicamento
    template_name = 'medicamento_confirm_delete.html'
    success_url = reverse_lazy('devices')


class UserCreateView(LoginRequiredMixin, EngenheiroRequiredMixin, View):
    def get(self, request):
        form = AdminUserCreateForm()
        return render(request, 'user_create.html', {'form': form})

    def post(self, request):
        form = AdminUserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
        return render(request, 'user_create.html', {'form': form})


class UserUpdateView(LoginRequiredMixin, EngenheiroRequiredMixin, UpdateView):
    model = CustomUser
    form_class = UserEditForm
    template_name = 'user_form.html'
    success_url = reverse_lazy('users')


class UserDeleteView(LoginRequiredMixin, EngenheiroRequiredMixin, DeleteView):
    model = CustomUser
    template_name = 'user_confirm_delete.html'
    success_url = reverse_lazy('users')


class DeviceCreateView(LoginRequiredMixin, EngenheiroRequiredMixin, CreateView):
    model = Device
    form_class = DeviceForm
    template_name = 'device_form.html'
    success_url = reverse_lazy('devices')


class DeviceUpdateView(LoginRequiredMixin, EngenheiroRequiredMixin, UpdateView):
    model = Device
    form_class = DeviceForm
    template_name = 'device_form.html'
    success_url = reverse_lazy('devices')


class DeviceDeleteView(LoginRequiredMixin, EngenheiroRequiredMixin, DeleteView):
    model = Device
    template_name = 'device_confirm_delete.html'
    success_url = reverse_lazy('devices')