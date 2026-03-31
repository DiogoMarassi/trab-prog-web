from django.shortcuts import render, redirect, get_object_or_404
from .models import Device, CustomUser

def home(request):
    return render(request, 'home.html')