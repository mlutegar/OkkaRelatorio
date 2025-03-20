# Etapa 1: Imagem base com Python
FROM python:3.11-slim

# Etapa 2: Define o diretório de trabalho dentro do container
WORKDIR /app

# Etapa 3: Copia os arquivos de dependências para o container
COPY requirements.txt /app/

# Etapa 4: Instala as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Etapa 5: Copia todo o código do projeto para o container
COPY . /app/

# Etapa 6: Configura variáveis de ambiente
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=OkkaRelatorio.settings

# Etapa 7: Exponha a porta 8000 para acessar o servidor Django
EXPOSE 8000

# Etapa 8: Comando padrão para iniciar o servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]