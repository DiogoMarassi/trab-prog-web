from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nome')),
                ('principio_ativo', models.CharField(max_length=150, verbose_name='Princípio Ativo')),
                ('dosagem', models.CharField(max_length=50, verbose_name='Dosagem (ex: 500mg, 10ml)')),
                ('quantidade', models.PositiveIntegerField(verbose_name='Quantidade em Estoque')),
                ('unidade', models.CharField(
                    choices=[
                        ('COMPRIMIDO', 'Comprimido(s)'),
                        ('CAPSULA', 'Cápsula(s)'),
                        ('FRASCO', 'Frasco(s)'),
                        ('AMPOLA', 'Ampola(s)'),
                        ('ML', 'mL'),
                        ('MG', 'mg'),
                    ],
                    default='COMPRIMIDO',
                    max_length=20,
                    verbose_name='Unidade',
                )),
                ('validade', models.DateField(verbose_name='Validade')),
                ('location', models.CharField(max_length=200, verbose_name='Localização (Ala/Armário)')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Última Atualização')),
            ],
            options={
                'verbose_name': 'Medicamento',
                'verbose_name_plural': 'Medicamentos',
                'ordering': ['name'],
            },
        ),
    ]
