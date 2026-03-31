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