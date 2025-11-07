# Program Pengelolaan Data Nilai Mahasiswa


## Cara Menjalankan

```bash
python program_nilai_simple.py
```

## Fitur Program

1. **Tampilkan Semua Data** - Lihat semua data mahasiswa dalam tabel
2. **Tambah Mahasiswa Baru** - Input data mahasiswa baru
3. **Cari Nilai Tertinggi** - Cari mahasiswa dengan nilai terbaik
4. **Cari Nilai Terendah** - Cari mahasiswa dengan nilai terendah
5. **Filter Berdasarkan Grade** - Filter mahasiswa by grade (A/B/C/D/E)
6. **Hitung Rata-rata Kelas** - Hitung rata-rata nilai kelas

## Fungsi-Fungsi

### 1. `hitung_nilai_akhir(uts, uas, tugas)`
Menghitung nilai akhir dengan bobot:
- UTS: 30%
- UAS: 40%
- Tugas: 30%

**Contoh:**
```python
nilai = hitung_nilai_akhir(80, 85, 90)
# Output: 85.0
```

### 2. `tentukan_grade(nilai)`
Menentukan grade berdasarkan nilai:
- A: ≥ 80
- B: ≥ 70
- C: ≥ 60
- D: ≥ 50
- E: < 50

### 3. `tampilkan_tabel(data)`
Menampilkan data mahasiswa dalam format tabel yang rapi.

### 4. `cari_tertinggi(data)`
Mencari mahasiswa dengan nilai akhir tertinggi.

### 5. `cari_terendah(data)`
Mencari mahasiswa dengan nilai akhir terendah.

### 6. `tambah_mahasiswa()`
Menambahkan data mahasiswa baru ke dalam list.

### 7. `filter_grade(data, grade_cari)`
Filter mahasiswa berdasarkan grade tertentu.

### 8. `hitung_rata_rata(data)`
Menghitung rata-rata nilai akhir seluruh kelas.

## Struktur Data

Program menggunakan **list** yang berisi **dictionary**:

```python
data_mahasiswa = [
    {
        "nama": "Budi Santoso",
        "nim": "23001",
        "nilai_uts": 85,
        "nilai_uas": 90,
        "nilai_tugas": 88
    },
    # ... mahasiswa lainnya
]
```