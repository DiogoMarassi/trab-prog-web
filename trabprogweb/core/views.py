from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Device
from .forms import DeviceForm

# -- Middleware de Blindagem Nível 2 (Verificação de Assinatura via Cookie no DB) --
class EngenheiroRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        # Valida se está logado e, rigorosamente, possui a Role apropriada ou permissão máxima de sistema
        return self.request.user.is_authenticated and (self.request.user.role == 'ENGENHEIRO' or self.request.user.is_superuser)
    
    def handle_no_permission(self):
        # Se um médico tentar forçar caminho, ignoramos a tela amarela feia do Django e redirecionamos pro UI Error state
        return render(self.request, '403.html', status=403)

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