# Gunakan base image Python yang ringan
FROM python:3.9-slim

# Tetapkan folder kerja di dalam container
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Salin script utama ke dalam container
COPY uts.py .

# Perintah yang dijalankan saat container start
CMD ["python", "uts.py"]
