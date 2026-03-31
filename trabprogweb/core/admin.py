from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Device

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'first_name', 'last_name', 'role', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        ('Perfil de Acesso ao Portal', {'fields': ('role',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Perfil de Acesso ao Portal', {'fields': ('role',)}),
    )

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'serial_number', 'device_type', 'status', 'location', 'updated_at')
    list_filter = ('status', 'device_type', 'manufacturer')
    search_fields = ('name', 'serial_number')
