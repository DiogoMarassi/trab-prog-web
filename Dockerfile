FROM python:3.12-slim

# Evita arquivos .pyc e garante logs em tempo real
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Instala dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o projeto Django (conteúdo de trabprogweb/)
COPY trabprogweb/ .

# Coleta os arquivos estáticos para a pasta staticfiles/
RUN python manage.py collectstatic --noinput

# Expõe a porta padrão do Cloud Run
EXPOSE 8080

# Roda as migrations e inicia o servidor com gunicorn
CMD ["sh", "-c", "python manage.py migrate && gunicorn trabprogweb.wsgi:application --bind 0.0.0.0:${PORT:-8080} --workers 2 --timeout 120"]
