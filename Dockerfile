# Imagen base con Python 3.11
FROM python:3.11-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos
COPY . .

# Instala dependencias
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expone el puerto (si estás usando Flask)
EXPOSE 5000

# Comando para ejecutar la app
CMD ["python", "app.py"]
