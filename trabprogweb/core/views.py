from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Device, CustomUser

@login_required
def home(request):
    devices = Device.objects.all()
    return render(request, 'home.html', {'devices': devices})