from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('novo/', views.DeviceCreateView.as_view(), name='device_create'),
    path('editar/<int:pk>/', views.DeviceUpdateView.as_view(), name='device_edit'),
    path('excluir/<int:pk>/', views.DeviceDeleteView.as_view(), name='device_delete'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]