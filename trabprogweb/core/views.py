from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Device
from .forms import DeviceForm

@login_required
def home(request):
    devices = Device.objects.all()
    return render(request, 'home.html', {'devices': devices})

class DeviceCreateView(LoginRequiredMixin, CreateView):
    model = Device
    form_class = DeviceForm
    template_name = 'device_form.html'
    success_url = reverse_lazy('home')