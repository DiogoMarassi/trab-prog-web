from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    class Role(models.TextChoices):
        MEDICO = 'MEDICO', 'Médico'
        ENGENHEIRO = 'ENGENHEIRO', 'Engenheiro/Administrador'

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.MEDICO,
        verbose_name="Perfil de Acesso"
    )

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"

class Device(models.Model):
    class Status(models.TextChoices):
        ATIVO = 'ATIVO', 'Ativo'
        MANUTENCAO = 'MANUTENCAO', 'Em Manutenção'
        INATIVO = 'INATIVO', 'Inativo'

    name = models.CharField(max_length=150, verbose_name="Nome do Dispositivo")
    serial_number = models.CharField(max_length=100, unique=True, verbose_name="Número de Série")
    device_type = models.CharField(max_length=100, verbose_name="Tipo de Aparelho")
    manufacturer = models.CharField(max_length=100, verbose_name="Fabricante")
    status = models.CharField(
        max_length=20, 
        choices=Status.choices, 
        default=Status.ATIVO, 
        verbose_name="Status Operacional"
    )
    location = models.CharField(max_length=200, verbose_name="Localização (Ala/Leito)")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última Atualização")

    class Meta:
        verbose_name = "Dispositivo"
        verbose_name_plural = "Dispositivos"
        ordering = ['-updated_at']

    def __str__(self):
        return f"{self.name} - S/N: {self.serial_number}"