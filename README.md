# Analisis Nilai Mahasiswa — UTS DevOps & Data Science

Aplikasi Python sederhana untuk menganalisis nilai mahasiswa dan menyimpan hasilnya ke database PostgreSQL, dikontainerisasi menggunakan Docker dan Docker Compose.

---

## Deskripsi Proyek

Script `uts.py` membaca data nilai 10 mahasiswa, menghitung statistik dasar (rata-rata, nilai tertinggi/terendah, jumlah lulus dan tidak lulus), lalu menyimpan hasilnya ke dalam database PostgreSQL.

---

## Arsitektur Sistem

Base image `python:3.9-slim` dipilih karena ukurannya yang ringan namun sudah cukup untuk menjalankan aplikasi Python beserta library yang dibutuhkan. Proyek ini terdiri dari dua container: `db` (PostgreSQL) dan `app` (Python). Keduanya berada dalam satu jaringan internal Docker, sehingga `app` bisa terhubung ke `db` menggunakan nama host `db`. Container `app` dikonfigurasi dengan `depends_on` agar selalu menunggu `db` siap terlebih dahulu. Data PostgreSQL disimpan menggunakan Docker Volume sehingga tidak hilang saat container dimatikan.

---

## Cara Menjalankan

**Prasyarat:** Docker Desktop sudah terinstall dan running.

**1. Clone repositori**
```bash
git clone https://github.com/Runyuk/uts-devops.git
cd uts-devops
```

**2. Jalankan aplikasi**
```bash
docker-compose up --build
```

**3. Matikan aplikasi**
```bash
docker-compose down
```
