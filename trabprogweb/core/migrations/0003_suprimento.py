from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_medicamento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suprimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nome')),
                ('categoria', models.CharField(
                    choices=[
                        ('UTENSILIO',   'Utensílio'),
                        ('EPI',         'EPI'),
                        ('DESCARTAVEL', 'Descartável'),
                        ('OUTRO',       'Outro'),
                    ],
                    default='UTENSILIO',
                    max_length=20,
                    verbose_name='Categoria',
                )),
                ('quantidade', models.PositiveIntegerField(verbose_name='Quantidade em Estoque')),
                ('unidade', models.CharField(
                    choices=[
                        ('UNIDADE', 'Unidade(s)'),
                        ('CAIXA',   'Caixa(s)'),
                        ('PACOTE',  'Pacote(s)'),
                        ('PAR',     'Par(es)'),
                        ('ROLO',    'Rolo(s)'),
                    ],
                    default='UNIDADE',
                    max_length=20,
                    verbose_name='Unidade',
                )),
                ('validade', models.DateField(blank=True, null=True, verbose_name='Validade (opcional)')),
                ('location', models.CharField(max_length=200, verbose_name='Localização (Ala/Armário)')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Última Atualização')),
            ],
            options={
                'verbose_name': 'Suprimento',
                'verbose_name_plural': 'Suprimentos',
                'ordering': ['name'],
            },
        ),
    ]
