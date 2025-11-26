# 🚀 Panduan Menjalankan Aplikasi Manajemen Matakuliah

Aplikasi API sederhana untuk mengelola data matakuliah menggunakan Pyramid Framework.

## 📋 Persyaratan Sistem
- Python 3.7 atau lebih baru
- pip (sudah terinstall dengan Python)

## ⚡ Langkah-Langkah Menjalankan Aplikasi

### 1. Masuk ke Direktori Proyek
```bash
cd muhammadfadhel_123140106_pertemuan6
```

### 2. Install Dependencies
```bash
pip install -e .
```

### 3. Setup Database
```bash
alembic upgrade head
```

### 4. Jalankan Server
```bash
pserve development.ini
```

### 5. Akses Aplikasi
Buka browser dan kunjungi: `http://127.0.0.1:6543`

## 🧪 Testing API

### Cara Mudah: Gunakan Script Testing
```bash
python test_api.py
```
Script ini akan otomatis:
- ✅ Test endpoint GET (list kosong)
- ✅ Tambah 3 data matakuliah awal
- ✅ Tampilkan hasil akhir

### Manual Testing dengan curl

#### Lihat semua matakuliah:
```bash
curl -X GET http://127.0.0.1:6543/api/matakuliah
```

#### Tambah matakuliah baru:
```bash
curl -X POST http://127.0.0.1:6543/api/matakuliah \
     -H "Content-Type: application/json" \
     -d '{"kode_mk": "IF101", "nama_mk": "Algoritma", "sks": 3, "semester": 1}'
```

#### Lihat detail matakuliah:
```bash
curl -X GET http://127.0.0.1:6543/api/matakuliah/1
```

#### Update matakuliah:
```bash
curl -X PUT http://127.0.0.1:6543/api/matakuliah/1 \
     -H "Content-Type: application/json" \
     -d '{"nama_mk": "Algoritma Lanjutan"}'
```

#### Hapus matakuliah:
```bash
curl -X DELETE http://127.0.0.1:6543/api/matakuliah/1
```

## 📊 API Endpoints

| Method | Endpoint | Deskripsi |
|--------|----------|-----------|
| GET | `/api/matakuliah` | List semua matakuliah |
| GET | `/api/matakuliah/{id}` | Detail matakuliah by ID |
| POST | `/api/matakuliah` | Tambah matakuliah baru |
| PUT | `/api/matakuliah/{id}` | Update matakuliah |
| DELETE | `/api/matakuliah/{id}` | Hapus matakuliah |

## 🔧 Troubleshooting

### ❌ Error: ModuleNotFoundError
**Solusi:**
```bash
pip install -e .
```

### ❌ Error: Database tidak ada
**Solusi:**
```bash
alembic upgrade head
```

### ❌ Error: Port 6543 sudah digunakan
**Solusi:** Edit file `development.ini`, ubah:
```ini
[server:main]
listen = localhost:6544
```

### ❌ Server tidak merespons
**Solusi:**
1. Pastikan server sudah berjalan: `pserve development.ini`
2. Cek port yang digunakan
3. Restart terminal jika perlu

## 📁 Struktur Proyek

```
muhammadfadhel_123140106_pertemuan6/
├── README.md           # Panduan ini
├── setup.py            # Konfigurasi package
├── development.ini     # Konfigurasi server
├── alembic.ini         # Konfigurasi database
├── test_api.py         # Script testing
├── matakuliah.db       # Database (dibuat otomatis)
├── alembic/            # Migration files
└── matakuliah_app/     # Kode aplikasi
    ├── __init__.py     # Setup Pyramid
    ├── models.py       # Model database
    └── views.py        # API endpoints
```

## 🎯 Status Testing

✅ **Model Data**: Lengkap dengan semua atribut dan constraints
✅ **API Endpoints**: Semua 5 endpoint CRUD berfungsi
✅ **Database**: SQLite dengan migrasi Alembic
✅ **Error Handling**: 400 dan 404 error handling
✅ **Testing**: Script otomatis tersedia

## 👨‍💻 Pengembang

Muhammad Fadhel - 123140106
Tugas Praktikum Pemrograman Web ITERA