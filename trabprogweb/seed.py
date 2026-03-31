import os
import django

# Setar o ambiente do django (com apontamento para a pasta configurada)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'trabprogweb.settings')
django.setup()

from core.models import CustomUser, Device

def seed_database():
    print("Iniciando injeção de dados no Banco de Dados SQLite...")

    # 1. Criação do Administrador Chefe do Portal
    if not CustomUser.objects.filter(username='admin').exists():
        CustomUser.objects.create_superuser('admin', 'admin@hospital.com', 'admin123', role='ENGENHEIRO')
        print("Superusuário admin criado (admin/admin123)")

    # 2. Criação de Contas Simples (Médico Vs Engenheiro)
    if not CustomUser.objects.filter(username='medico_teste').exists():
        CustomUser.objects.create_user('medico_teste', 'medico@hospital.com', 'teste123', role='MEDICO')
        print("Usuário Médico simulado criado (medico_teste/teste123)")

    if not CustomUser.objects.filter(username='engenharia_teste').exists():
        CustomUser.objects.create_user('engenharia_teste', 'engenharia@hospital.com', 'teste123', role='ENGENHEIRO')
        print("Usuário Engenheiro simulado criado (engenharia_teste/teste123)")

    # 3. Criação de Dispositivos (Frota Simulasda)
    if not Device.objects.exists():
        Device.objects.bulk_create([
            Device(name='Monitor Multiparamétrico XP', serial_number='MMP-2023-01', device_type='Monitor', manufacturer='Philips', status='ATIVO', location='UTI-A Leito 01'),
            Device(name='Ventilador Pulmonar Savina', serial_number='VP-8822-XY', device_type='Respirador', manufacturer='Dräger', status='MANUTENCAO', location='Setor B (Manutenção)'),
            Device(name='Bomba de Infusão Volumétrica', serial_number='BI-500-Z', device_type='Bomba', manufacturer='Baxter', status='ATIVO', location='Ala Pediátrica Leito 05'),
            Device(name='Eletrocardiógrafo Portátil MAC', serial_number='ECG-1122', device_type='Eletrocardiógrafo', manufacturer='GE Healthcare', status='INATIVO', location='Almoxarifado')
        ])
        print("Cadastro de 4 dispositivos físicos simulados efetuado.")

    print("Banco de dados pronto para o laboratório!")

if __name__ == "__main__":
    seed_database()
