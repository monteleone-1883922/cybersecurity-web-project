# Usa l'immagine ufficiale di Python
FROM python:3.9-slim

# Installa le dipendenze
RUN pip install flask requests

# Copia il file Python nell'immagine
COPY app.py /app/app.py

# Imposta la directory di lavoro
WORKDIR /app

# Esponi la porta 5000 (Flask default)
EXPOSE 5000

# Comando per avviare Flask
CMD ["python", "app.py"]
