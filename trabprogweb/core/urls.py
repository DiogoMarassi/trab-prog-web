from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('novo/', views.DeviceCreateView.as_view(), name='device_create'),
    path('editar/<int:pk>/', views.DeviceUpdateView.as_view(), name='device_edit'),
    path('excluir/<int:pk>/', views.DeviceDeleteView.as_view(), name='device_delete'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html', redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
]