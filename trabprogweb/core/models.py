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

class Medicamento(models.Model):
    class Unidade(models.TextChoices):
        COMPRIMIDO = 'COMPRIMIDO', 'Comprimido(s)'
        CAPSULA    = 'CAPSULA',    'Cápsula(s)'
        FRASCO     = 'FRASCO',     'Frasco(s)'
        AMPOLA     = 'AMPOLA',     'Ampola(s)'
        ML         = 'ML',         'mL'
        MG         = 'MG',         'mg'

    name            = models.CharField(max_length=150, verbose_name="Nome")
    principio_ativo = models.CharField(max_length=150, verbose_name="Princípio Ativo")
    dosagem         = models.CharField(max_length=50,  verbose_name="Dosagem (ex: 500mg, 10ml)")
    quantidade      = models.PositiveIntegerField(verbose_name="Quantidade em Estoque")
    unidade         = models.CharField(max_length=20, choices=Unidade.choices, default=Unidade.COMPRIMIDO, verbose_name="Unidade")
    validade        = models.DateField(verbose_name="Validade")
    location        = models.CharField(max_length=200, verbose_name="Localização (Ala/Armário)")
    updated_at      = models.DateTimeField(auto_now=True, verbose_name="Última Atualização")

    class Meta:
        verbose_name = "Medicamento"
        verbose_name_plural = "Medicamentos"
        ordering = ['name']

    def __str__(self):
        return f"{self.name} {self.dosagem} — {self.quantidade} {self.get_unidade_display()}"


class Suprimento(models.Model):
    class Categoria(models.TextChoices):
        UTENSILIO   = 'UTENSILIO',   'Utensílio'
        EPI         = 'EPI',         'EPI'
        DESCARTAVEL = 'DESCARTAVEL', 'Descartável'
        OUTRO       = 'OUTRO',       'Outro'

    class Unidade(models.TextChoices):
        UNIDADE = 'UNIDADE', 'Unidade(s)'
        CAIXA   = 'CAIXA',   'Caixa(s)'
        PACOTE  = 'PACOTE',  'Pacote(s)'
        PAR     = 'PAR',     'Par(es)'
        ROLO    = 'ROLO',    'Rolo(s)'

    name       = models.CharField(max_length=150, verbose_name="Nome")
    categoria  = models.CharField(max_length=20, choices=Categoria.choices, default=Categoria.UTENSILIO, verbose_name="Categoria")
    quantidade = models.PositiveIntegerField(verbose_name="Quantidade em Estoque")
    unidade    = models.CharField(max_length=20, choices=Unidade.choices, default=Unidade.UNIDADE, verbose_name="Unidade")
    validade   = models.DateField(null=True, blank=True, verbose_name="Validade (opcional)")
    location   = models.CharField(max_length=200, verbose_name="Localização (Ala/Armário)")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última Atualização")

    class Meta:
        verbose_name = "Suprimento"
        verbose_name_plural = "Suprimentos"
        ordering = ['name']

    def __str__(self):
        return f"{self.name} — {self.quantidade} {self.get_unidade_display()}"


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