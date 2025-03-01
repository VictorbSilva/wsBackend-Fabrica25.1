# Use uma imagem oficial do Python como base
FROM python:3.13.2


ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1


WORKDIR /app


RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY . .

# Use um usuário não-root para segurança
RUN useradd -m appuser && chown -R appuser /app
USER appuser

# Comando para executar o servidor (ajuste conforme sua necessidade)
CMD ["gunicorn", "projeto.wsgi:application", "--bind", "0.0.0.0:8000"]