from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Device
from .forms import DeviceForm


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


class LogoutView(View):
    def post(self, request):
        response = redirect('login')
        response.delete_cookie('access_token')
        response.delete_cookie('refresh_token')
        return response


@login_required
def home(request):
    devices = Device.objects.all()
    return render(request, 'home.html', {'devices': devices})


class DeviceCreateView(LoginRequiredMixin, EngenheiroRequiredMixin, CreateView):
    model = Device
    form_class = DeviceForm
    template_name = 'device_form.html'
    success_url = reverse_lazy('home')


class DeviceUpdateView(LoginRequiredMixin, EngenheiroRequiredMixin, UpdateView):
    model = Device
    form_class = DeviceForm
    template_name = 'device_form.html'
    success_url = reverse_lazy('home')


class DeviceDeleteView(LoginRequiredMixin, EngenheiroRequiredMixin, DeleteView):
    model = Device
    template_name = 'device_confirm_delete.html'
    success_url = reverse_lazy('home')