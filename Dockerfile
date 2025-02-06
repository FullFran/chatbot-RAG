# Usamos una imagen ligera de Python
FROM python:3.9-slim

# Definimos el directorio de trabajo como la raíz del proyecto
WORKDIR /app

# Copiamos todo el código de la aplicación
COPY . .

# Instalamos las dependencias
RUN pip install --no-cache-dir -r app/requirements.txt

# Exponemos el puerto 8000
EXPOSE 8000

# Ejecutamos FastAPI sin importar "app." explícitamente
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
