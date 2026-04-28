# Gunakan base image Python yang ringan
FROM python:3.9-slim

# Tetapkan folder kerja di dalam container
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY uts.py .

CMD ["python", "uts.py"]
