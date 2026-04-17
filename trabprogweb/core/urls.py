from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dispositivos/', views.devices_panel, name='devices'),
    path('dispositivos/novo/', views.DeviceCreateView.as_view(), name='device_create'),
    path('dispositivos/editar/<int:pk>/', views.DeviceUpdateView.as_view(), name='device_edit'),
    path('dispositivos/excluir/<int:pk>/', views.DeviceDeleteView.as_view(), name='device_delete'),
    path('usuarios/', views.users_panel, name='users'),
    path('usuarios/editar/<int:pk>/', views.UserUpdateView.as_view(), name='user_edit'),
    path('usuarios/excluir/<int:pk>/', views.UserDeleteView.as_view(), name='user_delete'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('registrar/', views.RegisterView.as_view(), name='register'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]