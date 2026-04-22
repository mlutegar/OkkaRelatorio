# ============================================
# Stage 1: Build React Frontend
# ============================================
FROM node:18-alpine as frontend-builder

WORKDIR /app/frontend

# Copia e instala dependências do frontend
COPY okkarelatorio-front/package*.json ./
RUN npm ci --production=false

# Copia código fonte e builda
COPY okkarelatorio-front ./
RUN npm run build

# Output: /app/frontend/build/ contém bundle.js, index.html, style.css, etc

# ============================================
# Stage 2: Django Backend Runtime
# ============================================
FROM python:3.11-slim

WORKDIR /app

# Instala dependências Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia build do frontend do Stage 1
COPY --from=frontend-builder /app/frontend/build ./frontend/build

# Copia resto do código Django
COPY . .

# Coleta arquivos estáticos para produção
RUN python manage.py collectstatic --noinput

ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=OkkaRelatorio.settings

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]