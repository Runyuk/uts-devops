import os
import pandas as pd
import psycopg2

#Data mahasiswa
data = {
    'Nama': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve',
             'Faris', 'Gita', 'Hendra', 'Indra', 'Julia'],
    'Nilai': [85, 90, 78, 92, 65, 88, 70, 55, 76, 95]
}

df = pd.DataFrame(data)

#Analisis data
df['Status'] = df['Nilai'].apply(
    lambda x: 'Lulus' if x >= 75 else 'Tidak Lulus'
)

rata_rata = df['Nilai'].mean()
nilai_max = df['Nilai'].max()
nilai_min = df['Nilai'].min()
jumlah_lulus = len(df[df['Status'] == 'Lulus'])
jumlah_tidak_lulus = len(df[df['Status'] == 'Tidak Lulus'])

print('=' * 40)
print('   ANALISIS NILAI MAHASISWA')
print('=' * 40)
print(df.to_string(index=False))
print('-' * 40)
print(f'Rata-rata Nilai  : {rata_rata:.2f}')
print(f'Nilai Tertinggi  : {nilai_max}')
print(f'Nilai Terendah   : {nilai_min}')
print(f'Jumlah Lulus     : {jumlah_lulus} mahasiswa')
print(f'Tidak Lulus      : {jumlah_tidak_lulus} mahasiswa')
print('=' * 40)

#Koneksi ke PostgreSQL
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_NAME = os.getenv('DB_NAME', 'nilaidb')
DB_USER = os.getenv('DB_USER', 'user')
DB_PASS = os.getenv('DB_PASS', 'password')

try:
    conn = psycopg2.connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )
    cursor = conn.cursor()

    # Buat tabel
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS hasil_nilai (
            id SERIAL PRIMARY KEY,
            nama VARCHAR(100),
            nilai INTEGER,
            status VARCHAR(20)
        )
    ''')

    # Simpan setiap baris data ke tabel
    for _, row in df.iterrows():
        cursor.execute(
            'INSERT INTO hasil_nilai (nama, nilai, status)'
            ' VALUES (%s, %s, %s)',
            (row['Nama'], row['Nilai'], row['Status'])
        )

    conn.commit()
    print('Data berhasil disimpan ke PostgreSQL!')
    cursor.close()
    conn.close()

except Exception as e:
    print(f'Gagal koneksi ke database: {e}')
