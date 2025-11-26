# Instruksi Setup PostgreSQL

Jika PostgreSQL belum terinstall, ikuti langkah berikut:

## 1. Download dan Install PostgreSQL
- Kunjungi: https://www.postgresql.org/download/windows/
- Download installer untuk Windows
- Jalankan installer dan ikuti wizard instalasi
- Catat password untuk user 'postgres'

## 2. Verifikasi Instalasi
Buka Command Prompt dan jalankan:
```cmd
psql --version
createdb --help
```

## 3. Setup Database
Setelah install, buka Command Prompt sebagai Administrator dan jalankan:
```cmd
createdb matakuliah_db
```

Atau gunakan pgAdmin:
- Buka pgAdmin
- Connect ke PostgreSQL server
- Buat database baru bernama 'matakuliah_db'

## 4. Update Konfigurasi (jika perlu)
Edit file `development.ini` dan ubah baris:
```
sqlalchemy.url = postgresql://postgres:[YOUR_PASSWORD]@localhost:5432/matakuliah_db
```
Ganti [YOUR_PASSWORD] dengan password PostgreSQL Anda.

## 5. Jalankan Setup Script
Setelah PostgreSQL siap, jalankan `setup.ps1` atau `setup.bat`.